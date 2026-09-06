# 项目状态协议

目标：把“做到哪了、确认了什么、剩下什么”从聊天记忆迁移到显式项目状态，解决长对话、上下文压缩、跨天继续和子Agent并行后的状态漂移。

## 四类状态文件

### 1. `PROJECT_STATE.md`
保存全局当前态：
- project_id / 更新时间
- 当前stage与current_object
- 当前active_batch
- 全片镜头数
- 全局locked_constraints
- completed_shots
- design_ready_shots
- production_ready_shots
- remaining_shots
- pending_verification
- 最近确认
- next_action

### 2. `SHOT_LEDGER.md`
每个镜头一行，至少：
`镜头｜A分析｜B设计｜确认状态｜C制作｜D验收｜当前版本｜风格/媒介｜依赖｜文件`

状态使用明确值：
- `todo`
- `in_progress`
- `ready`
- `confirmed`
- `complete`
- `blocked`
- `failed`
- `not_applicable`

不要只写模糊的“差不多/应该完成”。

### 3. `DECISIONS.md`
保存跨轮次仍有效的用户决策和锁定规则。

每条：
`Decision ID｜日期/顺序｜作用范围｜内容｜来源/原因｜是否仍有效`

例：
- 封面禁止最终大标题，但允许准确相关小字
- S03主体位置已确认，后续只改材质
- 全片016只借材质/布光，不自动继承全部构图

被用户撤销时标记 `superseded`，不要删除历史导致无法解释变化。

### 4. `shots/Sxx.md`
保存单镜头完整档案，是镜头级事实来源。

## 状态优先级

恢复任务时：
1. 用户本轮最新明确要求
2. `DECISIONS.md` 中仍有效的锁定规则
3. `PROJECT_STATE.md`
4. `SHOT_LEDGER.md`
5. 对应 `shots/Sxx.md`
6. 最近聊天补充
7. 更早的模糊记忆

发现文件互相冲突时，不默默猜。优先使用更新更晚且更具体的状态，并在本轮修正总账；涉及用户意图冲突时说明。

## 每轮更新顺序

完成一个镜头/批次后：
1. 先更新 `shots/Sxx.md`
2. 再更新 `SHOT_LEDGER.md`
3. 再汇总 `PROJECT_STATE.md`
4. 新增长期规则时更新 `DECISIONS.md`

不要先把PROJECT_STATE标完成，再留下镜头文件未完成。

## “剩下的”算法

用户说：
- “做剩下的”
- “剩余的继续”
- “其他镜头都做了”
- “开始做后面的”

先读取 `PROJECT_STATE.md + SHOT_LEDGER.md + relevant DECISIONS`，再根据最近明确目标stage计算。

### 如果最近目标是B设计
`remaining = A已完成 AND B != complete/ready/confirmed`

### 如果最近目标是C制作
优先：
`remaining = B已完成且达到当前制作前置要求 AND C != complete`

B未完成的镜头不自动越过B。只有用户明确说“剩下的直接做/不用确认/全部直接制作”时，才可对这些镜头按Skill允许的B+C合并规则执行。

### 如果用户只是说“继续”
按主Skill短指令解释，不把所有remaining自动加入授权范围。

执行前把计算出的列表显式写出，例如：
`本批剩余制作：S04、S05、S07；S06因数据待核暂时blocked。`

## active_batch

每次批量任务记录：
- batch_id
- stage
- authorized_scope
- started
- completed
- blocked
- remaining

用户中途打断或修改一个镜头，只改该批状态，不让其他已完成镜头回退。

## 长对话与上下文压缩

只要状态文件可访问：
- 不要求模型永久记住所有聊天
- 每次恢复复杂任务先读最小状态文件
- 具体做某镜头时再读对应 `shots/Sxx.md`
- 不为恢复状态重读全部历史对话或全部reference

如果状态文件不可访问，再使用最近聊天STATE锚点作为降级，并明确持久状态不可用。
