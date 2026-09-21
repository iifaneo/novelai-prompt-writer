<div align="center">

# NovelAI Prompt Writer

<p align="center">
  <b><a href="#-简体中文">🇨🇳 简体中文</a></b> | <b><a href="#-english">🇺🇸 English</a></b>
</p>

<p align="center">
  <em>A precise, hallucination-free prompt engineering tool & skill for NovelAI image generation.</em><br>
  <em>专为 NovelAI 打造的提示词编写、真实验证与自然语言平滑降级工具。</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/NovelAI-V5%20%7C%20V4-blue?style=flat-square" alt="NovelAI">
  <img src="https://img.shields.io/badge/Danbooru-API%20Verified-brightgreen?style=flat-square" alt="Danbooru">
  <img src="https://img.shields.io/badge/Python-3.8+-informational?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/Dependencies-Zero-success?style=flat-square" alt="Dependencies">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=flat-square" alt="License">
</p>

---

</div>

<a id="-简体中文"></a>
## 🇨🇳 简体中文

### 🌟 核心功能与设计原则

本工具严格遵循四步规范化工作流，专为追求画面精准可控的创作者设计：

#### 1. 最小化意图澄清与场景锚定
- **提取核心视觉要素**：自动解析主体、外观属性、动作、空间关系、构图镜头、光影与艺术风格。
- **杜绝冗长问卷**：信息足够时直接启动转译；若仅有基础灵感，主动提供 2~3 个差异化具体构思供选择，只做最小必要决策确认，不反复追问无关细节。
- **上下文一致性**：自动继承会话中前序确认的约束，精准识别并清除已废弃或撤销的旧要求。

#### 2. 严格的视觉增补确认边界
- **拒绝主观脑补**：任何新增的人物外观、服装细节、背景道具、特殊视角、光影配色或画师风格，均需得到明确确认。
- **拒绝垃圾词堆砌**：严禁无意义地添加所谓的“万能质量词/神级画质词”（如 `masterpiece`, `best quality` 等），保持 Prompt 干净高效。
- **保真转译自由**：翻译、等价近义词转换、标签去重与语序调优可在保持原意的前提下自动完成。

#### 3. Danbooru 官方真实验证与智能降级
- **官方 API 实时校验**：内置查词工具直连 Danbooru 公共接口，校验标签的真实存在性、使用热度（Post Count）与废弃状态（Deprecated）。
- **Wiki 释义语义消歧**：实时调取官方 Wiki 定义，严格比对标签含义是否与用户意图一致，拒绝仅凭字面相似而导致的语义偏差。
- **别名自动解析（Alias）**：自动将常见非标准表达、缩写或别名解析映射为 Danbooru 官方标准 Canonical 标签。
- **自然语言平滑降级（Fallback）**：当遇到复杂互动动作（如“谁对谁做什么”）、遮挡关系、特殊构图或找不到贴合标签时，自动采用精炼的英文自然语言描述，绝不强行拼凑生硬标签。
- **排除项语义保真**：遇到用户明确排除的元素时，严格避免将其正面化为正向标签。

#### 4. 纯净代码块交付
- **开箱即用**：交付结果统一封装在唯一的标准代码块中，可直接一键复制粘贴至 NovelAI 提示词输入框。
- **零视觉污染**：代码块内部不含多余标题、占位符、查词注释或废话。

---

### 🛠️ 快速安装与使用指南

#### 方式一：在支持 Skill / Agent 体系的 AI 客户端中使用
- **项目/工作区级安装**（推荐）：
  在你的项目根目录下创建 `.agents/skills/` 目录，将本文件夹放入：
  ```text
  你的项目根目录/
  └── .agents/
      └── skills/
          └── novelai-prompt-writer/
              ├── README.md
              ├── SKILL.md
              └── scripts/
                  └── lookup_danbooru.py
  ```
- **全局安装**：将本文件夹放置在你的个人 AI 配置目录中的 `skills/novelai-prompt-writer`。

#### 方式二：在 AI 代码编辑器中使用 (Cursor / Windsurf / Roo Code / Cline 等)
1. 将 `scripts/lookup_danbooru.py` 放入项目目录。
2. 将 `SKILL.md` 的内容添加到编辑器的规则配置中：
   - **Cursor**: 存为 `.cursor/rules/novelai.mdc` 或写入 `.cursorrules`
   - **Windsurf**: 写入 `.windsurfrules`
   - **Roo Code / Cline**: 写入 `.clinerules`
3. AI 编写提示词时，将自动调用 `python scripts/lookup_danbooru.py <tag>` 实时查证标签并遵循工作流规则。

#### 方式三：在 Web 网页端 AI 中使用 (ChatGPT / Claude / DeepSeek / Kimi 等)
- 将 `SKILL.md` 中的全部内容直接复制并粘贴到 **System Prompt（系统提示词）**、**Custom Instructions（自定义指令）** 或 **GPTs / Claude Projects** 的设定中即可。

#### 方式四：人类作为独立 CLI 命令行查词工具使用
```bash
python scripts/lookup_danbooru.py "1girl" "solo" "holding umbrella" "looking at viewer"
```

---

<p align="right"><a href="#novelai-prompt-writer">⬆ 返回顶部</a></p>

---

<a id="-english"></a>
## 🇺🇸 English

### 🌟 Core Features & Design Principles

This tool strictly follows a structured four-step workflow, engineered for creators seeking precision, fidelity, and zero hallucinations:

#### 1. Minimal Clarification & Scene Anchoring
- **Extract Essential Visual Elements**: Automatically parses subjects, visual attributes, actions, spatial relationships, framing/camera angles, lighting, and artistic styles.
- **No Tedious Questionnaires**: If the scene description is already actionable, conversion begins immediately. For raw ideas, proactively provides 2–3 distinct proposals to choose from with minimal necessary questions.
- **Contextual Consistency**: Carries forward confirmed constraints from prior turns and cleanly eliminates revoked requirements.

#### 2. Strict Confirmation Boundaries
- **Zero Hallucination / Invention**: Any newly proposed appearances, clothing, props, angles, lighting, or artist styles require explicit user confirmation before inclusion.
- **No Quality Word Spam**: Strictly prohibits injecting useless aesthetic/quality tokens (such as `masterpiece`, `best quality`), keeping prompts concise and effective.
- **Fidelity in Conversion**: Translation, synonymous mapping, deduplication, and syntax reordering are performed automatically while preserving exact intent.

#### 3. Official Danbooru Tag Verification & Smart Fallback
- **Live API Validation**: Direct integration with Danbooru's public API to verify exact tag existence, usage frequency (Post Count), and deprecation status.
- **Wiki Semantic Disambiguation**: Pulls official Wiki definitions on the fly to ensure tag meanings strictly match user intent, rejecting false matches based on superficial word overlap.
- **Automatic Alias Resolution**: Resolves non-standard variations and colloquial shorthands into official canonical tags.
- **Natural Language Fallback**: Automatically falls back to concise English prose when handling complex multi-subject interactions, occlusions, special perspectives, or rare concepts lacking accurate tags.
- **Exclusion Preservation**: Ensures negative constraints are faithfully respected without converting excluded concepts into positive tags.

#### 4. Clean Single Code-Block Delivery
- **Ready to Paste**: Returns the final prompt in a single clean code block ready to copy directly into NovelAI.
- **Zero Visual Noise**: No internal headers, markdown placeholders, verification logs, or chat filler inside the code block.

---

### 🛠️ Quick Installation & Setup

#### Method 1: AI Clients with Skill / Agent Support
- **Workspace-level Installation** (Recommended):
  Create a `.agents/skills/` directory in your project root and place this folder inside:
  ```text
  your-project-root/
  └── .agents/
      └── skills/
          └── novelai-prompt-writer/
              ├── README.md
              ├── SKILL.md
              └── scripts/
                  └── lookup_danbooru.py
  ```
- **Global Installation**: Place this folder inside your user-level skills directory (`skills/novelai-prompt-writer`).

#### Method 2: AI Code Editors (Cursor / Windsurf / Roo Code / Cline, etc.)
1. Place `scripts/lookup_danbooru.py` into your project directory.
2. Copy the contents of `SKILL.md` into your editor's rule configuration:
   - **Cursor**: Save as `.cursor/rules/novelai.mdc` or add to `.cursorrules`
   - **Windsurf**: Add to `.windsurfrules`
   - **Roo Code / Cline**: Add to `.clinerules`
3. The AI will automatically invoke `python scripts/lookup_danbooru.py <tag>` during prompt construction to verify tags in the background.

#### Method 3: Web-based AI Chatbots (ChatGPT / Claude / DeepSeek / Kimi, etc.)
- Copy the entire contents of `SKILL.md` directly into your **System Prompt**, **Custom Instructions**, or **GPTs / Claude Projects** instructions.

#### Method 4: Standalone Command-Line Lookup (CLI)
Anyone can use the lookup script directly from the terminal:
```bash
python scripts/lookup_danbooru.py "1girl" "solo" "holding umbrella" "looking at viewer"
```

---

## 📋 Repository Structure

```text
novelai-prompt-writer/
├── README.md               # Bilingual documentation & usage guide
├── SKILL.md                # Core prompt writing workflow & rules definition
└── scripts/
    └── lookup_danbooru.py  # Zero-dependency Danbooru API lookup tool
```

---

## ⚙️ Requirements

- **Python**: 3.8 or higher
- **Dependencies**: **Zero external dependencies** (Pure Python standard library: `http.client`, `urllib`, `json`, `argparse`). No `pip install` required.

---

<p align="right"><a href="#novelai-prompt-writer">⬆ Back to Top</a></p>
