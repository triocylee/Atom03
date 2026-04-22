# GJ Workspace

这个工作区用于“给定游戏名，快速复刻 Unity 核心体验”的多 Agent 并行流水线。

## 当前结构

- `agents/`: 可执行代理脚本
- `automation/`: 自动化入口脚本
- `docs/`: 已产出的文档与规则
- `projects/`: 仅保留模板（`_template`）
- `local_projects/`: 每次游戏名对应的本地实例（不入库）
- `archive/`: 归档历史产物

## 快速开始

1. 复制模板目录
2. 填写需求输入
3. 生成任务拆解
4. 并行执行 Code/Art
5. 人工测试收尾

## 新项目流程

1. 复制 `projects/_template` 为 `local_projects/<GameName>`
2. 编辑 `local_projects/<GameName>/spec/feature_input.json`
3. 依据 `docs/rules/AgentPool_Rules.md` 分配 Agent
4. 输出到 `local_projects/<GameName>/tasks/*` 与 `local_projects/<GameName>/assets/manifest/*`
5. 你执行人工测试并记录到 `local_projects/<GameName>/reports/`

## Unity 基座初始化

1. 创建本地实例
`powershell -ExecutionPolicy Bypass -File scripts/init_local_project.ps1 -GameName "<GameName>"`
2. 创建 Unity 工程骨架
`powershell -ExecutionPolicy Bypass -File scripts/bootstrap_unity_project.ps1 -GameName "<GameName>"`
3. 在 Unity Hub 打开
`local_projects/<GameName>/UnityProject`

## 模板仓库模式

1. 仓库主干只提交框架模板与规则，不提交具体游戏实例。
2. 每次新游戏实例都在 `local_projects/` 创建并本地协作。
3. 需要共享给帮手时，仅发送模板文件或本地实例快照，不回写到模板主干。

## 关键规则入口

- 架构说明: `docs/architecture/GJ_Architecture.md`
- 通用拆解: `docs/architecture/Universal_Decomposition_Framework.md`
- 并行规则: `docs/rules/AgentPool_Rules.md`
- 自动驾驶: `docs/rules/Autopilot_Mode.md`
- 模板仓库模式: `docs/rules/Template_Repo_Mode.md`
