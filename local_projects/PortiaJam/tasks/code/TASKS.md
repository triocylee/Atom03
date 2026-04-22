# Code Tasks - PortiaJam (Event P0)

范围锁定：仅实现赛事 P0。
不实现：`NPC` / `商会` / `剧情` / `P1-P3`。

## Gate A（场景、移动、采集、基础加工）

### PJ-A-CODE-001 SceneMain & Built-in Pipeline Baseline
- Inputs: 赛事规则（Built-in 管线要求）、资源包场景说明
- Outputs: `Assets/GameScene/SceneMain.unity` 可运行主场景、管线自检记录
- Dependencies: 无
- DoneCriteria: 工程为 Built-in；场景含野外+房屋外观；主要物体具碰撞

### PJ-A-CODE-002 Player Move/Jump/Gravity Controller
- Inputs: 键位映射方案、角色 prefab
- Outputs: 角色移动控制脚本、跳跃与重力参数配置、基础动画参数绑定
- Dependencies: PJ-A-CODE-001
- DoneCriteria: 角色可稳定移动/跳跃，跳跃受重力影响，无穿模卡死

### PJ-A-CODE-003 Gather Prompt + 3 Resource Nodes
- Inputs: 资源节点（木材/石头/铁矿）、交互触发距离
- Outputs: 交互提示UI触发、三类采集节点脚本、采集结果事件
- Dependencies: PJ-A-CODE-002
- DoneCriteria: 靠近资源显示提示；三类资源均可交互采集

### PJ-A-CODE-004 Tool Switch + Gather Animation Bridge
- Inputs: 工具映射、动画片段（CutTree*/Stone*/Saw*）
- Outputs: 交互触发自动切换工具逻辑、采集动画桥接层
- Dependencies: PJ-A-CODE-003
- DoneCriteria: 采集时切换对应工具并播放对应动作；动作结束后资源入包

### PJ-A-CODE-005 Basic Machine Craft (Cutting/Furnace)
- Inputs: 切割机/熔炉 prefab、基础配方与耗时
- Outputs: 机器交互脚本、加工队列/计时、产物入包逻辑
- Dependencies: PJ-A-CODE-004
- DoneCriteria: 两类机器均可交互加工；材料不足不可启动；产物正确发放

## Gate B（组装、生存、存档、提交流程）

### PJ-B-CODE-001 Assembly Table + Blueprint UI
- Inputs: 组装台 prefab、P0 图纸配置、材料规则
- Outputs: 图纸UI、材料校验器、组装产物生成逻辑
- Dependencies: PJ-A-CODE-005
- DoneCriteria: 可打开图纸UI；材料足够可组装，材料不足有明确提示

### PJ-B-CODE-002 Inventory UI & Count Sync
- Inputs: 物品ID表、背包格子配置、UI布局
- Outputs: 背包UI（材料/工具/数量）、数据绑定与刷新逻辑
- Dependencies: PJ-A-CODE-003
- DoneCriteria: 采集增加与制作消耗实时更新，UI与数据一致

### PJ-B-CODE-003 Survival Stats Feedback (P0 Minimal)
- Inputs: 生存值配置（至少体力+饱食度）
- Outputs: 生存值系统、阈值反馈（HUD/行动限制）
- Dependencies: PJ-B-CODE-002
- DoneCriteria: 生存值按规则变化并产生可见反馈，不阻断主链路

### PJ-B-CODE-004 Save/Load Snapshot + Scene Re-entry
- Inputs: 持久化字段清单（背包、组装结果、生存值、位置）
- Outputs: 存档结构、保存读取接口、坏档降级策略
- Dependencies: PJ-B-CODE-001, PJ-B-CODE-003
- DoneCriteria: 退出重进后关键状态恢复；坏档不崩溃且可回退默认态

### PJ-B-CODE-005 Event Submission Smoke Pack
- Inputs: 赛事提交要求、主流程冒烟清单
- Outputs: 三轮冒烟记录、已知问题清单、运行与提交流程说明
- Dependencies: PJ-B-CODE-004
- DoneCriteria: 连续3轮通过 `采集->加工/制作->组装建造->生存`；P0缺陷=0

## 可直接分发（A/B）

### A 负责人任务ID
- PJ-A-CODE-001
- PJ-A-CODE-002
- PJ-A-CODE-003
- PJ-B-CODE-002
- PJ-B-CODE-003
- PJ-B-CODE-004

### B 负责人任务ID
- PJ-A-CODE-004
- PJ-A-CODE-005
- PJ-B-CODE-001
- PJ-B-CODE-005

## 验收标准（统一）

1. 场景与角色满足赛事 P0：有野外与房屋外观、可移动跳跃且受重力。
2. 三种资源（木材/石头/铁矿）采集链路完整：提示 -> 交互 -> 工具/动作 -> 入包。
3. 基础加工机器（切割机、熔炉）和组装台图纸UI可用，材料校验正确。
4. 背包 UI 实时更新，主链路 10-15 分钟可稳定跑通。
5. 工程使用 Built-in 管线，`SceneMain` 可直接进入主流程。
6. 不得出现 NPC/商会/剧情及任意 P1-P3 功能入口。
