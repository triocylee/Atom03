# WORKLOAD_CHECK

## 人时与占比（Gate A + Gate B）

- 总人时: 28h
- Gate A（P0功能打通）: 14h
- Gate B（稳定、验收、提交）: 14h

## 模块量化（按赛事P0口径）

| Module | EffortPoint(1-5) | EstimatedHours | Gate | Owner | BackupOwner | Acceptance |
|---|---:|---:|---|---|---|---|
| SceneAndControllerP0 | 4 | 4.0 | A | Dev-A | Dev-B | 场景含野外+房屋外观且有碰撞；角色移动+跳跃+重力可用 |
| GatherAndToolActionP0 | 4 | 4.0 | A | Dev-A | Dev-B | 木/石/铁矿可采；靠近有提示；交互可自动切换工具与动作 |
| BasicMachineCraftP0 | 4 | 4.0 | A | Dev-B | Dev-A | 切割机/熔炉可交互并产出基础加工结果 |
| AssemblyAndBlueprintP0 | 4 | 4.0 | B | Dev-B | Dev-A | 组装台可开图纸UI；材料校验通过后可组装 |
| InventoryAndSurvivalP0 | 4 | 4.0 | B | Dev-A | Dev-B | 背包UI显示材料/工具/数量，采集与消耗实时更新；生存值可驱动反馈 |
| SaveLoadAndSceneEntry | 3 | 3.0 | B | Dev-A | Dev-B | SceneMain进主流程稳定；存档恢复背包/建造/生存关键状态 |
| SmokeRegressionAndSubmission | 4 | 5.0 | B | QA-A | QA-B | P0全链路3轮冒烟通过，提交包结构与说明齐全 |

## Gate 口径

### Gate A 出口条件

1. 完成 `场景与角色` + `采集系统` + `制作系统` 的赛事P0条目。
2. 资源类型固定为木材/石头/铁矿石，且交互提示、动作、入包链路完整。
3. 明确冻结不做项：NPC/商会/剧情与所有P1-P3。

### Gate B 出口条件

1. 完成 `组装台与图纸` + `背包UI` + `生存反馈` + `存档恢复`。
2. 可从 `Assets/GameScene/SceneMain.unity` 进入并跑通闭环。
3. P0阻断缺陷为0，交付说明包含管线要求（Built-in）与运行步骤。

## 备注

1. Unity 项目默认使用 `3D (Built-in Render Pipeline)`，禁止切到URP作为默认方案。
2. 若团队坚持URP，需单独列迁移风险，不计入P0必达路径。
3. Gate A 未通过前，不进入组装/提交联调。
