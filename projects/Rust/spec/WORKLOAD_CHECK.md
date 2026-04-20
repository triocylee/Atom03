# Rust - WORKLOAD_CHECK

## 人时与占比（1天冲刺）

- 总人时: 12h
- 你: 4h (33%)
- 帮手A: 3h (25%)
- 帮手B: 5h (42%)

## 模块量化

| Module | EffortPoint(1-5) | EstimatedHours | Owner | BackupOwner | Acceptance |
|---|---:|---:|---|---|---|
| Input | 2 | 1.2 | 你 | 帮手B | 移动、交互射线可用 |
| CoreLoop | 4 | 2.4 | 你 | 帮手B | 采集->制作->建造跑通 |
| EntityBehavior | 3 | 1.8 | 你 | 帮手B | 玩家与基础敌对行为可用 |
| ProgressSave | 2 | 1.2 | 帮手B | 你 | 关键状态可保存/恢复 |
| UIFeedback | 2 | 1.2 | 帮手A | 帮手B | HUD 可显示核心指标 |
| AssetMapping | 3 | 1.8 | 帮手A | 你 | 清单与占位资产一致 |
| TestAndDebug | 4 | 2.4 | 帮手B | 你 | 冒烟回归可复现可追踪 |

## 帮手B额外分担

1. 编写调试面板脚本（FPS、玩家状态、关键事件日志）
2. 编写一键冒烟脚本（核心流程检查）
3. 管理缺陷闭环（登记、回归、关闭）
