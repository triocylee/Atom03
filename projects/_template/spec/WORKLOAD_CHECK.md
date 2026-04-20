# WORKLOAD_CHECK

## 人时与占比（1天冲刺）

- 总人时: 12h
- 实现主线: 4h
- 资产与表现: 3h
- 测试与工具: 5h

## 模块量化

| Module | EffortPoint(1-5) | EstimatedHours | Owner | BackupOwner | Acceptance |
|---|---:|---:|---|---|---|
| Input | 2 | 1.2 | ToAssign | ToAssign | 输入稳定且无阻断 |
| CoreLoop | 4 | 2.4 | ToAssign | ToAssign | 主循环可跑通 |
| EntityBehavior | 3 | 1.8 | ToAssign | ToAssign | 关键实体行为可用 |
| ProgressSave | 2 | 1.2 | ToAssign | ToAssign | 关键状态可保存/恢复 |
| UIFeedback | 2 | 1.2 | ToAssign | ToAssign | HUD 与反馈完整 |
| AssetMapping | 3 | 1.8 | ToAssign | ToAssign | 资产清单可追踪 |
| TestAndDebug | 4 | 2.4 | ToAssign | ToAssign | 冒烟+回归+缺陷闭环 |

## 备注

1. 具体 Owner 分配由项目 Owner 在 Gate A 当天填写
2. 若模块复杂度变化，仅调整 EffortPoint 与工时，不改骨架
