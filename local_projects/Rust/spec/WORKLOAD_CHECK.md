# Rust - WORKLOAD_CHECK

## 人时与占比（1天冲刺）

- 总人时: 12h
- 实现主线: 4h
- 资产与表现: 3h
- 测试与工具: 5h

## 模块量化

| Module | EffortPoint(1-5) | EstimatedHours | Owner | BackupOwner | Acceptance |
|---|---:|---:|---|---|---|
| Input | 2 | 1.2 | ToAssign | ToAssign | 移动、交互射线可用 |
| CoreLoop | 4 | 2.4 | ToAssign | ToAssign | 采集->制作->建造跑通 |
| EntityBehavior | 3 | 1.8 | ToAssign | ToAssign | 玩家与基础敌对行为可用 |
| ProgressSave | 2 | 1.2 | ToAssign | ToAssign | 关键状态可保存/恢复 |
| UIFeedback | 2 | 1.2 | ToAssign | ToAssign | HUD 可显示核心指标 |
| AssetMapping | 3 | 1.8 | ToAssign | ToAssign | 清单与占位资产一致 |
| TestAndDebug | 4 | 2.4 | ToAssign | ToAssign | 冒烟回归可复现可追踪 |

## 附加分担（可选）

1. 编写调试面板脚本（FPS、玩家状态、关键事件日志）
2. 编写一键冒烟脚本（核心流程检查）
3. 管理缺陷闭环（登记、回归、关闭）
