# 差点后期

当前版本：**v3.0.3 · 标准渐进式 Skill + GPT Project 镜像**。

GitHub：`kzz-x/chadian-post-GTP-project`

## 推荐使用方式

### Agent / Skill 环境

正式 Skill 位于 `skill/`：

1. 以 `skill/SKILL.md` 为入口。
2. 按当前阶段和任务只读需要的 `skill/references/`。
3. 不预加载全部能力与18张风格卡。
4. 多镜头B/C批量任务读取 `parallel-execution.md`；有子Agent时可并行，无则顺序执行。
5. 长项目优先使用文件化工作区和状态总账，不依赖聊天记忆。

仓库根 `SKILL.md` 只是 launcher。

### ChatGPT GPT Project

1. 将 `project/01_项目指令.md` 放入 Project Instructions。
2. 上传 `project/来源/` 中的能力来源；风格优先使用 `project/来源/风格/000.md`～`017.md` 的拆分文件。
3. `project/来源/【差点风格】.md` 仅为旧版兼容，正常运行不要和拆分风格一起全量读取。
4. `project/模板/` 保存文件化项目状态模板，可用于长项目输出。

## v3核心变化

- **Prompt 自由度分级**：创作遵循 Explore → Select → Converge；P1 Creative Brief 用于自由探索，P2 Directed Creative 为大多数正式首版默认，P3 Execution Spec 只在精确落地/修改/修复时启用，避免长 Prompt 把 Agent 创造力锁死。
- **AI 友好运动预算**：镜头方案默认简单运镜 + 单一主动作，优先让 AI 做模型/场景/材质/灯光/可编辑底座；复杂 Camera / Hero Motion 明确留给人工接管。
- **封面产品真实性锁**：涉及具体品牌/型号时，先建立真实产品参考板并在 B0/B1/B2/C/D 持续显示准确性状态；没有可靠参考时优先只生成背景供后期PS真产品，若用户要求直接生成则明确标为示意占位。
- **并行制作**：主Agent可在B/C阶段对互不依赖的多个镜头调子Agent同步设计/制作；共享约束由主Agent冻结，最终由主Agent统一验收。
- **文件化交付**：全文分析、镜头总表、每个Sxx、实际成品都优先独立成文件，减少长聊天向上翻找。
- **外置记忆**：`PROJECT_STATE.md`、`SHOT_LEDGER.md`、`DECISIONS.md`、`shots/Sxx.md` 保存真实进度。“开始做剩下的”先读总账计算剩余集合。
- **Skill / Project同步**：`skill/` 是唯一真源；运行 `python scripts/sync_project_mirror.py` 同步，再运行 `python scripts/validate_sync.py` 校验。

## 标准工作区

```text
00_全文分析.md
01_镜头总表.md
PROJECT_STATE.md
SHOT_LEDGER.md
DECISIONS.md
shots/S01.md ...
outputs/S01/ ...
```

宿主支持附件/Artifact/文件卡时，Agent应暴露当前变更文件供点击、预览或下载；具体显示在侧栏、旁边还是消息区域由宿主UI决定。

## 版本管理

- `VERSION`：当前版本。
- `CHANGELOG.md`：版本变化与未测范围。
- `MAINTENANCE.md`：Skill→Project镜像维护规则。
- `archives/`：历史归档，不参与正常运行。

v3新增的15项行为eval目前已定义但尚未真实跑完 with-skill vs baseline，因此不能声称行为回归全部通过。
