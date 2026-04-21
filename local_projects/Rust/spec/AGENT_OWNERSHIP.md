# Rust 项目 Agent 写入边界

## Agent Pool

1. Planner
2. Gameplay
3. Systems
4. AssetOps
5. QA-Prep

## Ownership

1. Planner
- 可写: `projects/Rust/spec/*`, `projects/Rust/tasks/*`
- 禁写: Unity 源码目录

2. Gameplay
- 可写: `UnityProject/Assets/Scripts/Gameplay/*`
- 禁写: `Systems`, `UI`, `Data`

3. Systems
- 可写: `UnityProject/Assets/Scripts/Systems/*`, `UnityProject/Assets/Scripts/UI/*`
- 禁写: `Gameplay`

4. AssetOps
- 可写: `projects/Rust/assets/*`, `UnityProject/Assets/ArtPlaceholders/*`
- 禁写: `Scripts/*`

5. QA-Prep
- 可写: `projects/Rust/reports/*`
- 可写(工具层代码): `UnityProject/Assets/Scripts/Tools/*`, `UnityProject/Assets/Scripts/Debug/*`
- 禁写: `UnityProject/Assets/Scripts/Gameplay/*`

## Merge Rules

1. 同文件冲突优先保留拥有者版本
2. 跨模块接口变更必须由 Planner 审批后执行
3. 每日一次集成构建和冒烟
