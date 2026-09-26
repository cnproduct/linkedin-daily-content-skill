# LinkedIn Daily B2B Content Skill

为跨境 B2B 企业每日准备 4 张同主题图片和可直接发布的英文 LinkedIn 配文。默认方向：独特饮具与创意食品容器。

## 完整功能

- 12 类产品结构方向 × 12 种采购内容角度 × 5 种四图叙事结构，可组合选择并检查最近 14 天语义重复。
- 优先真实员工检查、包装发货、开发会议、匹配证书报告及真实产品照片；素材不足时调用内置 imagegen。
- 保留真实人物、现场和产品结构；AI 内容明确标记为概念示意，不冒充现有产品或已验证性能。
- 四张同主题高清正方形图，逐张核对英语、结构合理性、清晰度及手机阅读效果。
- 英文 B2B 配文，包含图片顺序、素材类型、主题和 AI 生成提示词。
- 从解码像素重建 PNG，清除 EXIF、caBX/JUMBF/C2PA，验证 CRC、图像可打开、像素不变、仅 IHDR/IDAT/IEND 数据块。
- 保留原图，清理失败不交付；完成后列出全部绝对路径。
- 支持每天 06:00 Asia/Shanghai 的 Codex 自动任务，实际更新后通过 Chrome 同步本仓库。

## 安装与使用

将本仓库复制到 `~/.codex/skills/linkedin-daily-content/`。安装依赖：`python -m pip install -r requirements.txt`。

调用：`使用 $linkedin-daily-content，为今天生成四张独特饮具/创意食品容器图片和英文配文。`

按 `references/local-profile.md` 调整素材路径和自动任务。调度由 Codex 自动任务提供，skill 文件本身不是常驻服务。内置 imagegen 无需单独提供 API Key。

检查历史：`python scripts/history.py "图片输出目录" --date YYYY-MM-DD`

清理图片：`python scripts/strip_png_metadata.py "图片绝对路径.png"`

独立验证：`python scripts/strip_png_metadata.py --verify "图片绝对路径.png"`

## 文件说明

`SKILL.md` 为入口；`references/theme-library.md` 为多样性选题库；`references/local-profile.md` 为路径与交付规则；`references/maintenance.md` 为验证和 GitHub 更新规则；`scripts/` 提供确定性历史检查和 PNG 清理验证。

只制作和保存素材，不自动发布 LinkedIn、不评论、不私信。不要上传日常成品、客户资料、员工照片、账号凭据到本技能仓库。同步任务需要本机运行且 Chrome/GitHub 登录可用。
