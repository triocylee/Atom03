# Thronefall M1 美术任务清单

## Header
- Game: Thronefall
- Milestone: M1
- Role: Art
- Scope baseline: core experience version

## Stage Goal
- 在不追求高精细的前提下，完成 M1 可玩所需的低模场景、建筑、敌人、UI 与基础特效资源，并满足程序可直接挂接。

## Must-Complete Items
1. 地图灰盒与王座、路径点可读。
2. 2 类建筑（箭塔、城墙）与 1 类敌人模型。
3. 占位 UI 图标与基础特效（攻击、受击、死亡）。

## Detailed Task Table
| ID | Task | Quantity/Scope | Naming | Deliverable Format | Receiver | Dependency | Start State | Done Criteria |
|---|---|---|---|---|---|---|---|---|
| A1 | 地图灰盒与地表材质 | 1 张 256x256 可战斗区域 | map_m1_* | FBX + PNG + 预览图 | Code | Code 提供地形尺寸 | Can start now | 可导入后路径无遮挡、王座区明确 |
| A2 | 王座与基础建筑低模 | 王座1、箭塔1、城墙1 | bld_m1_* | FBX + 贴图 | Code | Code 提供挂点命名 | Can start now | 程序可挂接碰撞和攻击点 |
| A3 | 敌人单位低模与动作 | 近战敌 1 套（走/攻/死） | enemy_m1_grunt_* | FBX 动画切片 | Code | Code 提供骨骼约束 | Wait | 夜晚波次可完整播放动作 |
| A4 | 建造与战斗 UI 图标 | 资源、建造、波次图标各 1 套 | ui_m1_icon_* | PNG/SVG | Code | UI 框架字段名 | Can start now | UI 可读取且尺寸统一 |
| A5 | 基础 VFX | 攻击命中/受击/死亡各 1 套 | vfx_m1_* | 序列帧或粒子配置 | Code | 事件触发点定义 | Wait | 事件触发后 200ms 内显示 |

## Execution Order
1. 先完成 A1+A2，保障关卡可运行。
2. 并行推进 A4，尽早接入 UI。
3. 收到代码事件点后完成 A3+A5。

## Handoff Rules
1. Art 每日 18:00 前提交当日资源包与变更清单。
2. Code 先集成后回写问题，不直接改资源源文件。
3. 任一命名不符合规范即阻断下游集成。

## Packaging Rules
- Folder layout: Art/M1/{Map,Building,Enemy,UI,VFX}
- Naming convention: {type}_m1_{name}_v{nn}
- Version tag format: v01, v02...

## Acceptance Checklist
1. 资源命名、目录、格式全部符合规范。
2. 程序可一次性导入，无丢贴图/丢骨骼。
3. QA 场景中可观察到资源正确加载。

## Risks and Recheck Plan
1. 风险：骨骼约束不一致导致动画错位。
2. 重检触发：Code 修改骨骼或挂点后全量重导。
