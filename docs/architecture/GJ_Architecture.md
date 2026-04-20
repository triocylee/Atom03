# GJ 架构与目录约定

## 目标

把“游戏机制拆解 -> 代码生成 -> 资产清单与占位填充 -> 人工测试收尾”固化为标准流水线。

## 分层

1. 输入层: `projects/<GameName>/spec/`
2. 规划层: `projects/<GameName>/tasks/`
3. 实现层: Unity 工程（外部或子目录）
4. 资产层: `projects/<GameName>/assets/`
5. 验证层: `projects/<GameName>/reports/`

## 标准目录

- `projects/<GameName>/spec/feature_input.json`
- `projects/<GameName>/tasks/art/`
- `projects/<GameName>/tasks/code/`
- `projects/<GameName>/tasks/qa/`
- `projects/<GameName>/assets/manifest/`
- `projects/<GameName>/assets/placeholders/`
- `projects/<GameName>/reports/`

## 产物契约

1. `spec/feature_input.json`
包含目标游戏、核心循环、平台、工期、限制条件。

2. `tasks/code/*.md`
每项任务要有输入、输出、验收标准、依赖。

3. `assets/manifest/*.md`
资产清单必须写明数量、命名规则、格式、来源策略。

4. `reports/*.md`
记录人工测试结论与阻塞项，只保留可执行结论。

## 节奏（1天冲刺）

1. 第 1-2 小时: 机制拆解 + 接口冻结
2. 第 3-8 小时: Code/Art 并行实现最小切片
3. 第 9-10 小时: 集成与冒烟
4. 第 11-12 小时: 你进行人工测试与收尾
