# 差点后期维护规则

`skill/` 是唯一 Source of Truth。`project/` 是 GPT Project 兼容镜像。

任何规则修改只有同时完成以下步骤才算完成：

1. 先修改 `skill/` 中的正式 Skill / references / assets / evals。
2. 运行 `python scripts/sync_project_mirror.py`。
3. 运行 `python scripts/validate_sync.py`。
4. 必要时更新 `skill/evals/evals.json`。
5. 更新 VERSION / CHANGELOG / README。
6. 提交 Git。

正常创作运行不要读取本文件。

## 镜像范围

- `skill/references/post-details.md` → `project/来源/【差点后期】.md`
- `visual.md` → `【差点视觉】.md`
- `footage.md` → `【差点素材】.md`
- `elements.md` → `【差点元素】.md`
- `clips.md` → `【差点片段】.md`
- `motion.md` → `【差点动效】.md`
- `ai-motion-core.md` → `【AI动效开发核心经验】.md`
- `cover.md` → `【差点封面】.md`
- `assets.md` → `【差点资产】.md`
- `qa.md` → `【差点质检】.md`
- `parallel-execution.md` → `【差点并行】.md`
- `artifact-output.md` → `【差点交付】.md`
- `project-state.md` → `【差点状态】.md`
- `skill/references/styles/` → `project/来源/风格/`
- 工作区模板 → `project/模板/`

`project/来源/【差点风格】.md` 保留作旧版兼容；正式渐进运行优先 `project/来源/风格/`。
