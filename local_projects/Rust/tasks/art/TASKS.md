# Rust Core Experience - Art Tasks

## Stage Goal

提供可运行的占位与灰盒资产，支持代码联调，不追求最终商业品质。

## Task Cards

| TaskID | Inputs | Outputs | Dependencies | DoneCriteria |
|---|---|---|---|---|
| A-001 | 机制拆解 | 玩家第一人称手部占位模型 1 套 | None | 在近战/采集动作时无严重穿模 |
| A-002 | C-002 | 资源节点：树/石头/麻纤维各 2 变体 | C-002 | 节点可区分类型且被采集后可替换破碎态 |
| A-003 | C-004 | 物品图标：基础工具/食物/建造件共 24 个 | C-004 | 图标命名与配方 ID 一一对应 |
| A-004 | C-005 | 建造件模型：地基/墙/门/门框/箱子 | C-005 | Pivot 与尺寸符合 1m 网格拼接规则 |
| A-005 | C-006,C-007 | UI 资源：生命/饥饿/口渴条与受击反馈 | C-006,C-007 | HUD 可读性通过 1080p/2K 测试 |
| A-006 | C-007 | 基础敌对生物 1 套（模型+动作占位） | C-007 | 敌方巡逻/追击/攻击动画可正常循环 |
| A-007 | C-010 | 环境灰盒包：地形材质、岩石、植被、天空盒 | C-010 | 场景可达 30FPS+（测试机基线） |

## Naming Convention

1. 模型: `mdl_<category>_<name>_v001`
2. 贴图: `tex_<category>_<name>_<type>_v001`
3. 图标: `ico_item_<name>_v001`

## Deliverables

1. 模型: FBX
2. 纹理: PNG/TGA
3. 图标: PNG (512x512)
4. 动画: FBX 或 Unity Clip
