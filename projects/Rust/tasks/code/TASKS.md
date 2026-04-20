# Rust Core Experience - Code Tasks

## Stage Goal

在 1 天内完成单人可玩的 Rust 核心体验最小切片：采集、制作、建造、生存。

## Task Cards

| TaskID | Owner | Inputs | Outputs | Dependencies | DoneCriteria |
|---|---|---|---|---|---|
| C-001 | Gameplay | `feature_input.json` | FPS 移动与交互射线系统 | None | 可移动、跳跃、冲刺，交互射线可命中资源节点 |
| C-002 | Gameplay | C-001 | 资源采集系统（节点耐久/掉落） | C-001 | 木头石头采集可入包，节点被采空后刷新 |
| C-003 | Systems | C-002 | 背包系统（堆叠、拖拽、丢弃） | C-002 | UI 可查看并操作库存，容量与堆叠规则生效 |
| C-004 | Systems | C-003 | 制作队列（配方、时长、产出） | C-003 | 可排队制作斧子/火把/门，计时完成后入包 |
| C-005 | Gameplay | C-004 | 建造放置（地基/墙/门）与碰撞检测 | C-004 | 可预览放置、旋转、合法检测与确认建造 |
| C-006 | Systems | C-001 | 生存指标（生命/饥饿/口渴）衰减逻辑 | C-001 | 指标按时间衰减，低阈值触发扣血 |
| C-007 | Gameplay | C-001,C-006 | 基础敌对AI（巡逻/追击/攻击） | C-001,C-006 | 夜晚触发刷怪，AI 可攻击玩家且可被击杀 |
| C-008 | Systems | C-003,C-006 | 主 HUD + 菜单 + 提示文案系统 | C-003,C-006 | HUD 显示指标和快捷栏，提示文本可配置 |
| C-009 | Systems | C-003,C-005,C-006 | 存档系统（背包/建造/时间） | C-003,C-005,C-006 | 退出重进后可恢复关键状态 |
| C-010 | Integrator | 全部模块 | 一键启动场景与集成冒烟脚本 | C-001..C-009 | 30 分钟连续运行无阻断性错误 |

## One-Day Cutline (必须当日完成)

1. C-001 FPS移动与交互
2. C-002 采集
3. C-003 背包
4. C-004 制作队列（仅3个配方）
5. C-005 建造放置（仅地基/墙/门）
6. C-006 生存指标
7. C-008 HUD

## Stretch (有余量再做)

1. C-007 基础敌对AI
2. C-009 存档
3. C-010 集成脚本

## Execution Order

1. C-001, C-006 并行启动
2. C-002 -> C-003 -> C-004
3. C-005 与 C-007 并行
4. C-008 -> C-009
5. C-010 收口

## Write Boundary

1. Gameplay Agent 仅写 `Scripts/Gameplay/*`
2. Systems Agent 仅写 `Scripts/Systems/*` 与 `Scripts/UI/*`
3. Integrator 负责 `Scenes/*`、`Bootstrap/*`
