# 通用拆解与分配框架（任意游戏名可用）

## 目的

不依赖具体游戏类型，统一通过“模块骨架 + 复杂度评分 + 角色配额”完成稳定拆解与分配。

## Step 1: 模块骨架

1. Input
2. CoreLoop
3. EntityBehavior
4. ProgressSave
5. UIFeedback
6. AssetMapping
7. TestAndDebug

## Step 2: 复杂度评分

每个模块打分 `1-5`：

1. 规则复杂度
2. 交互复杂度
3. 数据状态复杂度
4. 依赖复杂度

模块总分 = 四项平均后四舍五入。

## Step 3: 工时估算

1. 一天冲刺基线总量: `12 人时`
2. 模块工时 = `12 * (模块分 / 所有模块分总和)`
3. 允许误差: `±15%`

## Step 4: 角色分配（默认）

1. Owner
- 拆解、接口冻结、主循环关键代码

2. Helper A
- 资产清单、占位资产、表现层接线

3. Helper B
- 测试执行、回归闭环、工具层代码、部分系统代码

说明：具体占比由 Owner 在 `WORKLOAD_CHECK.md` 中按当日资源填写。

## Step 5: Gate A 必交付

1. `spec/feature_input.json`
2. `spec/AGENT_OWNERSHIP.md`
3. `spec/WORKLOAD_CHECK.md`

## WORKLOAD_CHECK 最小字段

1. Module
2. EffortPoint
3. EstimatedHours
4. Owner
5. BackupOwner
6. Acceptance
7. Risk
