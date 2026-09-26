# Search First｜先搜，再做

用于差点后期 B/C 阶段的上层搜索门禁。目标不是“所有任务都上网”，而是避免 AI 在已有事实、成熟参考或现成资产存在时凭空编造和重复造轮子。

核心顺序：

**Search → Select → Design → Build**

## 1｜三种独立 Gate

### Truth / Evidence First
回答“真实世界里它到底是什么”。

强制触发：
- 具体品牌、产品、型号、零件、设备、UI、Logo、参数、结构；
- 新闻、发布会、时间线、标准、规格等事实型内容；
- 工业 / 机械 / 生物 / 物理关系不能靠想象补齐。

### Reference First
回答“成熟的人是怎么设计、怎么动的”。

强制触发：
- 新封面 / KV / 产品广告；
- UI / HUD / 高级 Typography / Camera / Transition；
- Motion taste、构图、材质、灯光、节奏决定质量；
- 人、动物、生物动作、液体、碰撞、布料、跌落、复杂机械运动；
- 用户反馈“太模板 / 一眼 AI / 动作不自然”。

详细规则：`reference-first.md`。

### Asset First
回答“有没有东西可以直接拿来用”。

强制触发：
- 有明确语义的 Icon / Symbol / Logo / Emoji / UI Asset；
- Animated Icon / Icon Morph / Lottie；
- 通用 3D Icon / 3D Model / Props；
- HDRI / Texture / Material；
- 官方产品 PNG / SVG / Press Kit / 品牌资源；
- 标准工业符号、图表符号、成熟模板或组件。

详细规则：`asset-first.md` 与 `assets.md`。

## 2｜阶段边界

- A｜全文分析：不外搜；只在镜头卡标记 `TRUTH_NEED / REFERENCE_NEED / ASSET_NEED`。
- B｜指定对象设计：允许且应主动完成必要的 Truth / Reference / Asset Search；搜索属于设计，不等于进入制作。
- C｜指定制作：优先使用 B 已锁定结果；完成下载、本地化、导入和集成。关键项仍为 `UNSEARCHED` 时不得无依据直接自制。
- D｜修改：已有锁定参考 / 资产继续复用；只有修改目标改变时才补搜。

用户明确要求“不要搜 / 只按我给的 / 必须原创”时，以用户最新要求为准，但事实准确性不能伪造。

## 3｜什么可以不搜

通常不需要外搜：
- 矩形、圆、线、纯装饰几何；
- 已有模板内的小 Patch；
- 改字、改色、改位置、改尺寸；
- 明确给定数据的简单图表；
- 用户已提供且明确锁定的完整参考 / 资产。

**简单 ≠ 可以跳过 Asset First。**
例如 cloud-upload 图标虽然简单，但属于成熟语义资产，仍应先检索；一个普通圆形则无需检索。

## 4｜最小搜索交付

B 阶段只保留真正有用的结果，不堆链接：

`类型｜候选｜来源/许可｜约束或用途｜采用/备选/淘汰原因`

进入 C 前，凡命中 Asset First 的对象应能归入：
- `READY`
- `USER_PROVIDED`
- `PLACEHOLDER_APPROVED`
- `NOT_APPLICABLE`

`UNSEARCHED` 不能进入正式制作。
