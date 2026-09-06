# 差点动效｜数据图表

必须记录来源、原始值、单位、时间、地区/人群/产品范围、统计口径、实测/预测/估计、转换计算。

20%→30%：增加**10个百分点**，相对增长**50%**，不能混用。

规则：柱形从零基线；时间间隔按实际比例；缺失值不当零；饼图分母统一；实测/预测明显区分；不用装饰性3D改变数据长度；数字动画与图形长度共享同一数据源；终态必须等于原始数据。

## dataConfig

```js
const dataConfig = {
  title: "",
  unit: "",
  scope: {},
  status: "pending",
  sources: [],
  series: [],
  notes: [],
  precision: 1,
  missingValuePolicy: "gap"
};
```

视觉、时间、布局分别放`visualConfig`、`timelineConfig`、`layoutConfig`。不要把正式数据散落硬编码在多个图层。
