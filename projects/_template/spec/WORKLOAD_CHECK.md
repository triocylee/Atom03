# WORKLOAD_CHECK

## 人时与占比（1天冲刺）

- 总人时: 12h
- 你: 4h (33%)
- 帮手A: 3h (25%)
- 帮手B: 5h (42%)

## 模块量化

| Module | EffortPoint(1-5) | EstimatedHours | Owner | BackupOwner | Acceptance |
|---|---:|---:|---|---|---|
| Input | 2 | 1.2 | 你 | 帮手B | 输入稳定且无阻断 |
| CoreLoop | 4 | 2.4 | 你 | 帮手B | 主循环可跑通 |
| EntityBehavior | 3 | 1.8 | 你 | 帮手B | 关键实体行为可用 |
| ProgressSave | 2 | 1.2 | 帮手B | 你 | 关键状态可保存/恢复 |
| UIFeedback | 2 | 1.2 | 帮手A | 帮手B | HUD 与反馈完整 |
| AssetMapping | 3 | 1.8 | 帮手A | 你 | 资产清单可追踪 |
| TestAndDebug | 4 | 2.4 | 帮手B | 你 | 冒烟+回归+缺陷闭环 |

## 备注

1. 帮手B默认承担最多工作量（测试与工具层代码）
2. 若模块复杂度变化，仅调整 EffortPoint 与工时，不改骨架
