# NovelAI Prompt Writer (Antigravity Skill - Lite Edition)

NovelAI 图像生成提示词编写与校对 Skill。专注于将中文场景描述精准转换为 Danbooru 标签与自然语言混合的优质 Prompt，杜绝无依据的脑补与堆砌。

## 🌟 特性

- **极简确认**：支持最小化意图澄清，严格确认画面新增元素。
- **真实查证**：调用 Danbooru 官方公开 API 实时校验标签与 Wiki 释义，避免虚构拼写与过时词汇。
- **智能降级**：遇到复杂空间、互动动作或无对应标签时，自动采用精炼的英文自然语言（Natural Language）表达。
- **纯净交付**：直接输出可供复制的单一代码块，不混杂多余解释。
- **轻量零依赖**：仅需 Python 3.8+ 标准库，无需 `pip install` 任何额外依赖包。

---

## 🚀 安装步骤

### 方法一：全局安装（所有工作区通用，推荐）

将 `novelai-prompt-writer` 文件夹复制到你的系统配置目录中：

- **Windows**: `%USERPROFILE%\.gemini\config\skills\novelai-prompt-writer`
  *(通常为 `C:\Users\<用户名>\.gemini\config\skills\novelai-prompt-writer`)*
- **macOS / Linux**: `~/.gemini/config/skills/novelai-prompt-writer`

### 方法二：单工作区安装（仅在指定项目生效）

在你的项目根目录下创建 `.agents/skills/` 目录，将 `novelai-prompt-writer` 文件夹放置其中：
```text
你的项目根目录/
└── .agents/
    └── skills/
        └── novelai-prompt-writer/
            ├── SKILL.md
            ├── README.md
            └── scripts/
                └── lookup_danbooru.py
```

---

## 📖 使用方法

安装完成后无需任何额外配置。在 Antigravity 聊天中直接用自然语言描述你想绘制的画面即可，例如：

> **“帮我写一个 NovelAI 提示词：夜雨中的霓虹商业街，一位撑着透明雨伞、身穿黑色风衣的长发少女，看向镜头。”**

AI 助手将自动激活该 Skill，查验 Danbooru 标签并为你生成格式规范的最终 Prompt。
