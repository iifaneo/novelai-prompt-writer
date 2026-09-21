---
name: novelai-prompt-writer
description: Write or revise NovelAI image prompts from scene descriptions, using Danbooru-verified tags and natural-language fallback. Use when the user wants a copyable image prompt with control over every added visual element.
---

# NovelAI Prompt Writer

Turn the user's intended scene into one complete, copyable Prompt. Follow the four rules below in order. Keep this skill focused on prompt writing.

## 1. Establish the scene with minimal clarification

1. Extract the user's explicit subjects, attributes, actions, relationships, setting, composition, lighting, style, and exclusions. These are reading categories, not required fields to fill in.
2. Carry forward still-applicable requirements from the conversation. Remove requirements the user has replaced or withdrawn. Distinguish user-approved details from earlier assistant suggestions.
3. If the description expresses a usable scene, proceed directly to conversion. Missing optional details do not make a description incomplete. Honor an explicit request to convert only the supplied description without expansion.
4. If the user has supplied only a seed idea and needs a direction, proactively offer two or three short, distinct scene proposals in one interaction. Keep the original idea intact and state the proposed additions explicitly. Let the user choose, combine proposals, or supply their own description.
5. Ask only for the smallest decision needed to proceed. After the reply, use the selected or supplied details and leave other gaps unspecified. Do not launch another round of optional questions or present a comprehensive questionnaire.
6. If a contradiction prevents faithful conversion, ask one focused question about that contradiction; combine it with the clarification round when possible. Do not resolve it by inventing scene content.

## 2. Confirm every added visual element

1. Before adding content, classify it as either a faithful expression of an approved detail or a new visual decision.
2. Translation, equivalent wording, tag conversion, reordering, and deduplication may proceed without confirmation when they preserve meaning.
3. New subjects, appearance, clothing, actions, expressions, props, surroundings, camera choices, lighting, colors, styles, or artist influences require explicit confirmation before inclusion. Do not add stock quality or aesthetic terms merely to make a prompt look complete.
4. Present necessary proposed additions together, preferably in the initial scene proposals. Selecting a proposal confirms only the details actually stated in it; it does not authorize unstated embellishments. Partial approval confirms only the approved portion.
5. Silence, ambiguity, a general request to improve the prompt, or an unselected proposal is not approval of a specific addition. Omit optional unapproved additions instead of asking indefinitely. If a further addition is truly necessary, obtain confirmation before using it.
6. Apply the same boundary during revisions. Change only what the user requested or approved and retain other applicable constraints.

## 3. Convert approved meaning into verified tags

1. Split the approved scene into concepts and relationships. Identify candidate tags without treating recalled spellings or familiar-looking phrases as verified.
2. Check each candidate against accessible first-party Danbooru tag records or wiki pages using [scripts/lookup_danbooru.py](scripts/lookup_danbooru.py), which calls the public JSON API: `python <skill-directory>/scripts/lookup_danbooru.py rain "looking at viewer"`. The script uses only the standard library and returns source URLs, retrieval times, exact records, and wiki definitions where available. A web-search fetch error alone does not establish that the official API is unavailable. Review the returned definition against the approved scene; a script retrieves evidence, not semantic approval. Missing wiki text or a deprecated tag requires further first-party review or natural-language fallback. No exact record means that spelling was not found, not that no corresponding concept exists. Resolve aliases to their supported canonical tag when first-party evidence establishes that mapping. Reuse evidence already checked in the current task.
3. Keep a lightweight working record of the source and verification result for each tag. Search snippets, mirrors, third-party lists, and example prompts can suggest candidates but do not establish direct Danbooru verification. Never describe partial coverage as verification of the whole prompt.
4. Use a verified tag only when its meaning matches the approved concept. Reject a near match that introduces a different action, identity, setting, style, or other unapproved meaning. Do not infer a match from word overlap alone.
5. When no suitable verified tag is found, express the original concept in concise natural language. Keep relationships and complex actions in natural language when individual tags would lose who does what to whom. Do not force a tag-to-prose ratio or repeat a concept in both forms without a concrete need.
6. If access prevents verification, distinguish that from finding no matching tag. If only web retrieval failed, try the public API helper once. It stops further requests after an access failure; do not repeatedly rerun a blocked batch. Respect authentication requirements, rate limits, and explicit access denials; do not disable TLS checks or attempt to bypass challenges. Preserve the affected meaning in natural language and briefly disclose the verification limitation at delivery. Do not pass an unchecked candidate off as a verified tag.
7. Preserve exclusions without turning excluded concepts into positive tags. Use faithful natural-language wording when the intended restriction cannot otherwise be represented within the requested Prompt.
8. Danbooru verification establishes tag identity and semantic fit, not guaranteed NovelAI recognition or generation quality. Do not claim generation success without generation evidence. Consult current official NovelAI documentation if model-specific syntax is actually needed; do not add weights, special syntax, or model assumptions by habit.

## 4. Check and deliver one complete Prompt

1. Compare every visual statement against the approved scene. Remove unapproved additions, revoked requirements, contradictions, and unnecessary duplicates.
2. Check that every approved detail is represented, every tag has direct supporting evidence, and every remaining unsupported concept is expressed as natural language. Recheck any tag introduced during final editing.
3. Proofread the final text for malformed tags, broken syntax, accidental fragments, and lost relationships or exclusions.
4. Return the complete Prompt in a single fenced code block. The block contains only text intended to be pasted into the Prompt field, with no headings, placeholders, verification annotations, or explanations inside it.
5. By default, add no tag explanations, evidence tables, alternate prompts, or separate UC block. Briefly state a material verification limitation outside the block when needed. Provide additional material only when the user explicitly requests it or a higher-priority instruction requires it.
