# Asset First｜现成资产优先

核心原则：

**有成熟、准确、授权清晰的现成资产时，先复用或改造；确认没有合适资产后，才允许 AI / AE / Blender 从零生成或重画。**

## 1｜强制触发对象

以下对象默认必须先做 Asset Search：
- 语义图标、UI Symbol、标准箭头、文件类型、天气 / 网络 / 设备图标；
- Logo、品牌标识、官方产品图、Press Kit；
- Animated Icon、Lottie、Icon Morph；
- Emoji、标准符号、工业符号；
- 通用 3D Icon、3D Model、Props；
- HDRI、Texture、Material；
- 可复用 UI Component、图表组件、成熟模板。

以下通常可直接制作：
- 无语义的圆 / 线 / 矩形 / 自定义装饰；
- 已锁定设计里的局部几何；
- 数据本身决定的简单图形。

## 2｜来源优先级

1. 当前项目 / Style Pack / Template 已有资产
2. 用户提供资产
3. 官方品牌 / 产品 / Press Kit
4. 结构化开源 Asset Registry / 官方开源库
5. 授权清晰的专业素材库
6. AI / AE / Blender 自制
7. 明确标注的 Placeholder

优先选择 Agent 友好的来源：API / JSON Registry / CLI / MCP / npm / raw SVG / direct download。

## 3｜搜索完成条件

Asset Search 不是“打开过网站”。
至少需要：
- 用中文和英文 / 常见同义词搜索；
- 找到 1–3 个真实候选，或明确确认没有合适候选；
- 核对格式、许可和是否适合当前风格；
- 决定：直接用 / 改造 / Morph / 转 Shape / 作为占位 / 放弃。

禁止编造不存在的图标名、下载地址、模型、许可或库能力。

## 4｜Asset Manifest

进入正式制作前，对命中对象保持极短清单：

```text
ASSET PREFLIGHT
READY | cloud-upload | Tabler | SVG | MIT
READY | microphone | Lucide | SVG | ISC
PLACEHOLDER_APPROVED | industrial-connector | no suitable asset
```

状态：
- `READY`
- `USER_PROVIDED`
- `PLACEHOLDER_APPROVED`
- `NOT_APPLICABLE`
- `UNSEARCHED`

正式 BUILD 前不得保留应搜索对象的 `UNSEARCHED`。

## 5｜与 Reference First 的关系

Asset First 解决“拿什么现成东西”，Reference First 解决“画面 / 动作应该怎么设计”。

两者可独立触发：
- “云上传图标” → Asset First
- “高级文字转场” → Reference First
- “iOS 风格云上传状态动画” → Asset First + Reference First

找到资产后仍要统一颜色、线宽、材质、比例和 Motion，不把不同图库默认风格直接拼贴。
