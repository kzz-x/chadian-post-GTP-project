# 【差点资产】

- **负责什么**：为图标、界面、时间轴、图表、三维与现成动效选择成熟库和资产，减少重复开发，统一工程配置。
- **何时调用**：动效/封面/元素需要标准图标、品牌资源、可编辑组件、缓动、图表、模型辅助或现成矢量动画。
- **何时不要调用**：不为“调用资产库”额外加无关效果；纯文字回答不装依赖；素材候选的事实核验仍属【差点素材】。
- **常见触发词**：图标、组件、开源库、现成资产、SVG、UI、GSAP、D3、Rive、Lottie、Three.js。
- **输入**：所需功能/视觉、现有框架、目标导出方式、平台性能、许可证要求和可用工具。
- **输出**：B交资产选型与用途/接入计划；获授权查找/制作后交实际来源、版本/许可、集成结果与替代方案。


## 阶段与交付

按【差点后期】阶段控制。A/B只基于项目已有资料列选型，不安装库、不写工程、不外搜；用户明确“查这个库/找图标”可执行指定检索。C才核当前API/许可并实际集成。

B固定清单：`功能｜成熟资产/库｜为什么适合本镜头｜已有依赖/新增项｜可改参数｜后续验证方式`。C固定交：`实际资产入口/版本/许可｜集成用途｜已实现可改项｜验证结果｜依赖与本地化状态`。不能只列GSAP/D3等名称却交自画临时图标和不可控动画；未使用的库不谎称已集成。

## 1. 选用原则

AI 优先调成熟资产，不重复造轮子。优先已有工程依赖、官方资源、可直接用的 SVG/源码，再选择新增库；每加一个依赖都说明实际用途。不是必须调用全部目录。

免费/开源、无需登录、可控制样式且可复用的资产优先，但开源代码许可证不等于其中每个素材或品牌标识的授权。目录是来源整理时的官方入口，使用时核查当前可用性、版本 API 与具体许可，不承诺永久免费或无需注册。

标准图标不要用 AI 栅格图替代 SVG；真实 Logo 需核对版本和品牌规范。外部组件先看代码/依赖/许可，再运行或安装，不盲目执行陌生脚本；连接器不可用则用允许的公开资源与现有工程，不假称已连接某服务。

## 2. 高频目录

| 类别/成熟库 | 入口 | 什么时候选 / 怎样接入 |
|---|---|---|
| Iconify | [iconify.design](https://iconify.design/) | 跨图标集检索；按实际图标 ID 取 SVG/组件，不编名称 |
| Lucide | [lucide.dev](https://lucide.dev/) | 常用线性 UI/参数图标默认；统一描边与尺寸 |
| Tabler | [tabler.io/icons](https://tabler.io/icons) | Lucide 缺特定符号时补充；统一线宽避免混风格 |
| Phosphor | [phosphoricons.com](https://phosphoricons.com/) | 同系列多权重/双色层次；同画面少混权重 |
| Simple Icons | [simpleicons.org](https://simpleicons.org/) | 品牌 SVG 补充入口；核对当前品牌标识与许可，找不到回官方 |
| shadcn/ui | [ui.shadcn.com](https://ui.shadcn.com/) | 已有 React 工程的控制面板、表单、卡片；复制/registry 集成，按当前依赖核查 |
| Radix | [radix-ui.com](https://www.radix-ui.com/) | 可访问交互基础：滑块、弹层、选择；视觉由工程统一 |
| Magic UI | [magicui.design](https://magicui.design/) | 找合适的卡片/边框/轻动效实现；提取单一机制，重写视觉 token |
| Aceternity | [ui.aceternity.com](https://ui.aceternity.com/) | React 视觉模块参考；不直接把网页 Hero 当视频画面 |
| 21st.dev | [21st.dev](https://21st.dev/) | 检索可改造组件；逐组件核查依赖与使用条款 |
| GSAP | [gsap.com](https://gsap.com/) | 连续主时间轴、暂停/seek、复杂进入退出；按当前官方 API 接入 |
| Motion | [motion.dev](https://motion.dev/) | 已有 React/适合的界面动画；确保生产视频仍受统一时间控制 |
| Anime.js | [animejs.com](https://animejs.com/) | 轻量 DOM/SVG/数值动画；使用项目实际版本，不混旧新 API |
| Remotion | [remotion.dev](https://www.remotion.dev/) | React 程序化视频、按帧输出和批量模板；核查当前使用许可 |
| D3 | [d3js.org](https://d3js.org/) | 自定义 scale、axis、shape、data binding；视觉和时间轴由工程统一 |
| ECharts | [echarts.apache.org](https://echarts.apache.org/) | 常规到复杂图表快速生产；关闭无关交互，定制主题和动画 |
| Observable Plot | [observablehq.com/plot](https://observablehq.com/plot/) | 快速验证数据与图形关系；满足需求可直接定制为成品 |
| Vega-Lite | [vega.github.io/vega-lite](https://vega.github.io/vega-lite/) | 声明式数据图与可重复规格；需要精细镜头节奏时加统一控制 |
| Three.js | [threejs.org](https://threejs.org/) | 真正的三维结构、相机与材质需求；不是默认科技背景方案 |
| React Three Fiber（R3F） | [r3f.docs.pmnd.rs](https://r3f.docs.pmnd.rs/) | 已有 React 三维工程，复用 Three 场景组件 |
| drei | [drei.docs.pmnd.rs](https://drei.docs.pmnd.rs/) | R3F 的相机/环境/资产等辅助；只取所需，避免默认漂浮抢戏 |
| Lottie | [lottie.github.io](https://lottie.github.io/) | 已有 JSON 矢量动效；控制播放、速度、尺寸，确认渲染特性 |
| Rive | [rive.app](https://rive.app/) | 已有 .riv 和状态机；使用实际 inputs/runtime，不编造资产内部状态 |

字体优先复用批准字体或 [Fontsource](https://fontsource.org/) 的可自托管资源；需要检索可用 [Google Fonts](https://fonts.google.com/)。中文字体覆盖、字重和实际授权逐项检查。背景图案/纹理优先少量已有 SVG/CSS；普通背景能用基础图形清楚完成，就不新增大型特效库。

## 3. 接入最短路径

1. 确认当前工程框架、版本与实际功能，再查官方文档/本地依赖；不要照旧记忆拼安装命令。
2. 选择一个主库或最少组合。例如单文件参数动效用 SVG＋GSAP；精确图表再加 D3 必需模块；已有 React 面板用 shadcn/Radix，不为一枚图标迁移框架。
3. 统一色彩、线宽、圆角、字体、阴影、缓动、时长到 config；图标 viewBox、尺寸与基线对齐。不要把不同库的默认设计混贴。
4. 图表数据遵循【差点动效】，装饰不能改变数据结构或比例。复杂光影独立层，前景数据和文本仍可编辑。
5. 接到统一时间 t；库自身循环、随机数、自动播放须受控，保证 seek 和导出一致。Lottie/Rive 不支持当前导出目标时先验证或转合适预渲染资产。
6. 记录实际资产来源/版本/许可和修改范围。需要联网的字体、库、图片有可行的本地化或降级；不要仅靠在线嵌入留一个无法重开的工程。

## 4. 集成验收

确认真实加载、没有缺字体/空图标、许可适用、样式统一、时间可控、手机性能可接受、输出效果正确。遇到库不可用优先现有依赖、官方 SVG/简化组件；允许实现小而明确的自定义缺口，但不要重写成熟框架。

交付只列本项目实际用到的资产和用途，不把整个目录附在每次回答中。资产检索没有结果如实说明，不能声称某库“有”未找到的图标、品牌或动画。
