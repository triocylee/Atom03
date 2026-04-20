# Thronefall M1 测试任务清单

## Header
- Game: Thronefall
- Milestone: M1
- Role: QA
- Scope baseline: core experience version

## Stage Goal
- 建立 M1 冒烟与首轮回归基线，快速识别阻断闭环问题，确保每日构建可验证、可复现、可回归。

## Must-Complete Items
1. 覆盖开局->建造->夜战->结算的 smoke 清单。
2. 首轮功能回归（资源、放置、波次、结算）。
3. 缺陷提单规范与复测机制。

## Detailed Task Table
| ID | Task | Quantity/Scope | Naming | Deliverable Format | Receiver | Dependency | Start State | Done Criteria |
|---|---|---|---|---|---|---|---|---|
| Q1 | 冒烟用例设计 | 核心流程 15 条 | tc_m1_smoke_* | 用例文档 + 执行记录 | Code | C1-C3 首包 | Can start now | 15 条用例均可执行 |
| Q2 | 每日构建冒烟 | 每日 1 次全流程 | rpt_m1_daily_* | 测试日报 | Code/PM | C6 构建包 | Wait | 当日阻断问题 100% 提交 |
| Q3 | 首轮功能回归 | 建造/战斗/结算 30 条 | tc_m1_reg_* | 回归报告 | Code | C4-C5 合入 | Wait | 关键模块无 P0 遗留 |
| Q4 | 缺陷提单与跟踪 | P0-P2 分级 + 复现步骤 | bug_m1_* | 缺陷单（含日志/截图） | Code | 任一测试执行 | Can start now | 每单可复现、可验证修复 |
| Q5 | 美术集成复测 | 动画/VFX/UI 集成后专项 10 条 | tc_m1_artreg_* | 复测记录 | Art/Code | A3-A5 合入 | Wait | 资源替换无功能回退 |

## Execution Order
1. 先完成 Q1，并对首包执行基线冒烟。
2. 进入每日 Q2，持续阻断问题前置。
3. C4/C5 稳定后执行 Q3，最后做 Q5。

## Handoff Rules
1. QA 仅基于 Code 提供的带版本号构建执行。
2. 缺陷必须包含版本号、复现步骤、期望与实际。
3. Art 集成后由 QA 发起专项复测结论回传 Code。

## Packaging Rules
- Folder layout: QA/M1/{cases,reports,bugs,evidence}
- Naming convention: {type}_m1_{module}_{date}
- Version tag format: build+case 双标签（例 m1.r03 + smoke.v02）

## Acceptance Checklist
1. 每日构建均有冒烟结论。
2. P0 缺陷当日可见并跟踪到关闭。
3. 回归报告可追溯到具体构建版本。

## Risks and Recheck Plan
1. 风险：资源替换导致隐性碰撞或事件丢失。
2. 重检触发：任意地图、骨骼、波次脚本变更后重跑 smoke+专项回归。
