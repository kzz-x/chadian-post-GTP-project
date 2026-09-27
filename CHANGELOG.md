# 更新记录

## v3.0.3 — 2026-09-27

- 新增 **Prompt Freedom Mode**：P1 Creative Brief / P2 Directed Creative / P3 Execution Spec。
- 默认工作流改为 **Explore → Select → Converge**：探索阶段保留模型创意空间，大多数正式首版使用 Directed Creative，只有精确落地、复刻、Bug 修复与 D 阶段修改才进入 Execution Spec。
- 新增 **Constraint Budget**：区分 LOCKED / DIRECTED / FREE，避免把 Visual Anchor 已经说明的内容再次翻译成逐帧、逐层、坐标化长 Prompt。
- 新增“只收紧失败维度”规则：首次结果偏离时不整体加长 Prompt，只精确约束构图、节奏、主体行为等实际失败项。
- 同步差点后期正式 Skill、GPT Project 镜像与项目指令。
- 新增行为 eval 18–19，覆盖自由探索与局部收敛；本次仅完成规则与测试定义，未实际跑完整模型行为回归。

## v3.0.2 — 2026-09-24

- 新增 **AI 友好运动预算 / Simple Motion First**：AE、Blender、CGI 与程序化动效方案默认先保证模型/场景/构图/材质/灯光，再以固定镜头或单一轻推/轻移/轻绕配合少量持续运动完成表达。
- 不再为了“高级感”默认设计复杂 Camera choreography、多段连续变形或高难度动作衔接；只有叙事确实不可替代时才升级。
- 复杂 Motion 必须在方案阶段标记 `AI易失败 / 建议人工接管`，推荐 AI 先搭 Scene / LookDev / Rig / 基础动画，再由人工完成复杂 Camera、主 Graph、Path 与最终节奏。
- 已同步 `skill/references/motion.md`、`clips.md` 与 GPT Project 镜像；本次为规则更新，未做模型行为回归。

## v3.0.1 — 2026-09-21

- 【差点封面】新增 **Product Accuracy Lock / 产品真实性锁**：具体品牌/型号封面强制显示 Product Accuracy Status，并贯穿 B0/B1/B2/C/D。
- 产品类封面新增独立 Product Reference Board，优先官方/可信真实图，多角度核验；用户提供的准确参考优先级最高。
- 新增 A/B/C 三种产品制作模式：参考锁定完整生成、背景+真实产品PS（默认优先）、无参考示意占位。
- 没有可靠产品参考时允许继续生成，但必须明确“仅示意/待PS替换”，不得把 AI 近似产品当准确成品；产品准确性优先于画面完整度。
- 更新封面行为 eval，覆盖“无产品图先设计”和“明确直接生成但无参考”两类场景。
- 规则已同步 Skill 与 Project 镜像；本次仅做静态规则/镜像一致性核对，未跑完整模型行为回归。

## v3.0.0 — 2026-09-06（当前版本）

- 按标准 Skill Progressive Disclosure 重构：`skill/SKILL.md` 只做阶段机与路由，能力、风格按需读取。
- 000–017 风格卡拆为独立文件；Project 镜像新增 `来源/风格/`，旧【差点风格】仅保留兼容。
- 新增【差点并行】：B/C批量镜头可由主Agent调度子Agent并行；先冻结共享约束、判断依赖，主Agent统一回读和质检。
- 新增【差点交付】：A/B/C/D阶段成果优先写独立可点击/预览/下载文件；每镜维护稳定 `shots/Sxx.md`。
- 新增【差点状态】：`PROJECT_STATE.md + SHOT_LEDGER.md + DECISIONS.md + shots/Sxx.md` 成为长对话外置状态；“剩下的”按总账计算，不凭模型记忆。
- 新增工作区模板与 `scripts/sync_project_mirror.py` / `validate_sync.py`，正式 Skill 为唯一真源，Project 为兼容镜像。
- eval 扩展到15项，新增并行、文件化交付、剩余镜头恢复、无子Agent降级用例。
- 结构和镜像规则已写入仓库；15项行为eval尚未实际跑 with-skill vs baseline，不声称全部通过。

## v2.0.0 — 2026-09-05

- 输入全文先分析，按A分析/B设计/C指定制作/D验收改稿推进。
- 总览后逐镜头八项分析卡；稳定镜头编号，固定能力交付模板。
- 实际读取来源并说明关键约束；生成前提供完整提示词。
- 封面保留用户横竖标题区；禁止最终大标题和杂字，允许少量准确、有用途的小字。
- 不满意先诊断；保留已确认文字策略、画幅、主体、字体与编辑功能。
- HTML图层、关键帧、完整保存重开、撤销重做及手机操作必须实际验收。
- 风格000–017共18张卡专业正文保留。
- 用户初步实测反馈“还行”；未提供完整回归日志。

## v1.0.0 — 2026-09-05（历史版本，不建议启用）

- 首次整合原始来源，整理为项目指令及正式来源。
- 插座实测暴露越阶段制作、分析过粗、Prompt缺失、封面文字漂移与工程功能不足，后由v2修正。

## 发布规则

每次记录动机、变化、验证结果和未测范围。Skill规则修改必须同步Project镜像并运行同步校验；新版本保留独立提交和可恢复历史。
