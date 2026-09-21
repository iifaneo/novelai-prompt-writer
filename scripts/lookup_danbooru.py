"""Fetch exact tag records and wiki definitions from Danbooru's public API."""

import argparse
from datetime import datetime, timezone
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_URL = "https://danbooru.donmai.us"


def fetch(resource, field, value):
    query = urlencode({f"search[{field}]": value, "limit": 10})
    url = f"{BASE_URL}/{resource}.json?{query}"
    request = Request(url, headers={
        "User-Agent": "NovelAI-Prompt-Writer/1.0 (public tag lookup)",
        "Accept": "application/json",
    })
    with urlopen(request, timeout=15) as response:
        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            raise ValueError("Expected JSON; received a page or challenge instead")
        data = json.load(response)
    if not isinstance(data, list):
        raise ValueError("Expected a list of API records")
    return {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "records": data}


def lookup(tag, result):
    tags = fetch("tags", "name", tag)
    result["tag_source"] = tags
    matches = [record for record in tags["records"] if record.get("name") == tag]
    if not matches:
        result["status"] = "no_exact_tag_record"
        return
    record = matches[0]
    result["tag"] = record
    wiki = fetch("wiki_pages", "title", tag)
    result["wiki_source"] = wiki
    definitions = [page for page in wiki["records"]
                   if page.get("title") == tag and not page.get("is_deleted")]
    result["wiki"] = definitions[0] if definitions else None
    if record.get("is_deprecated"):
        result["status"] = "deprecated_tag_requires_review"
    elif definitions:
        result["status"] = "exact_tag_and_wiki_found"
    else:
        result["status"] = "exact_tag_found_without_wiki"
    result["semantic_fit"] = "requires_review_against_approved_scene"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tags", nargs="+", help="Exact candidate tags; quote spaces")
    args = parser.parse_args()
    results = []
    blocked = False
    for supplied in dict.fromkeys(args.tags):
        tag = supplied.strip().lower().replace(" ", "_")
        result = {"requested": supplied, "query": tag}
        results.append(result)
        if not tag or any(char in tag for char in "*?\r\n"):
            result["status"] = "invalid_exact_query"
            continue
        if blocked:
            result["status"] = "not_attempted_after_access_failure"
            continue
        try:
            lookup(tag, result)
        except HTTPError as error:
            result.update(status="access_failed", error=f"HTTP {error.code}")
            blocked = True
        except (URLError, TimeoutError, OSError, ValueError) as error:
            result.update(status="access_failed", error=str(error))
            blocked = True
    print(json.dumps({"source": BASE_URL, "results": results},
                     ensure_ascii=True, indent=2))
    return 1 if any(item["status"] in {
        "access_failed", "not_attempted_after_access_failure", "invalid_exact_query"
    } for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
