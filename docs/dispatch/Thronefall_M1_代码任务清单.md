# Thronefall M1 代码任务清单

## Header
- Game: Thronefall
- Milestone: M1
- Role: Code
- Scope baseline: core experience version

## Stage Goal
- 完成 M1 最小玩法闭环：白天建造、夜晚波次、防御塔攻击、王座受击、胜负结算，并形成可持续集成给 QA 的构建包。

## Must-Complete Items
1. 日夜状态机与波次调度。
2. 建造扣费、建筑放置校验、防御塔自动攻击。
3. 王座生命、失败结算、重开流程。

## Detailed Task Table
| ID | Task | Quantity/Scope | Naming | Deliverable Format | Receiver | Dependency | Start State | Done Criteria |
|---|---|---|---|---|---|---|---|---|
| C1 | 游戏状态机 | Day/Night/Result 三状态 | sys_state_m1_* | 源码模块 + 配置 | QA | 无 | Can start now | 状态切换可重复 20 次无异常 |
| C2 | 资源与建造系统 | 1 货币、2 建筑、放置碰撞检测 | sys_build_m1_* | 源码 + JSON 配置 | Art/QA | UI 占位资源 | Can start now | 资源不足/位置冲突提示正确 |
| C3 | 敌人波次与寻路 | 3 波固定脚本 + 1 类敌人 | sys_wave_m1_* | 源码 + 波次表 | QA | 地图导航网格 | Can start now | 敌人可达王座且路径稳定 |
| C4 | 战斗结算 | 塔攻击、敌人受伤、死亡移除 | sys_combat_m1_* | 源码模块 | QA | Art 动画/VFX 占位 | Wait | 夜晚全波次可正确结算 |
| C5 | 胜负与重开 | 王座血量归零失败，守完胜利 | sys_result_m1_* | UI 触发逻辑 + 场景重置 | QA | C1-C4 | Wait | 失败/胜利后 1 键重开成功 |
| C6 | 构建与日志 | 每日可运行包 + 关键事件日志 | build_m1_* | 可执行包 + changelog | QA | 全系统 | Can start now | QA 可按日志复现问题 |

## Execution Order
1. 先做 C1+C2+C3 打通基础链路。
2. 再接 C4 完成战斗闭环。
3. 最后 C5+C6 固化交付节奏。

## Handoff Rules
1. Code 先给 Art 输出资源规格：尺寸、骨骼、挂点、命名。
2. 每次集成后打包给 QA，并附变更列表。
3. QA 的 P0/P1 缺陷在下一构建优先修复。

## Packaging Rules
- Folder layout: Build/M1/{bin,data,logs,notes}
- Naming convention: thronefall_m1_build_{yyyymmdd}_{rev}
- Version tag format: m1.r{nn}

## Acceptance Checklist
1. 新开局到结算流程可完整运行。
2. 关键交互（建造、战斗、结算）均有日志。
3. 无阻断级崩溃和脚本报错。

## Risks and Recheck Plan
1. 风险：波次脚本与寻路冲突导致卡怪。
2. 重检触发：地图/导航改动后重跑全波次回归。
