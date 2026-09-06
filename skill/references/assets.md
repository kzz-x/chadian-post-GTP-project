# 【差点资产】

原则：**成熟资产优先，不重复造轮子。**

常用类别：图标 Iconify/Lucide/Tabler/Phosphor/Simple Icons；UI shadcn/ui/Radix；动画 GSAP/Motion/Anime.js；图表 D3/ECharts/Observable Plot/Vega-Lite；三维 Three.js/R3F/drei；视频 Remotion；矢量动效 Lottie/Rive；字体使用批准字体、Fontsource、Google Fonts等。

优先已有依赖；一个功能尽量一个主库；不无故叠GSAP+Motion+Anime；标准图标不用AI栅格图替代SVG；品牌Logo核对版本；外部代码先看来源/依赖/许可；统一颜色、线宽、圆角、字体、阴影和缓动；接入统一时间`t`；自动循环和随机效果必须受控；联网依赖要有本地化/降级方案；未真实集成的库不能说已使用。
