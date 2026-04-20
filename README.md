# GJ Workspace

这个工作区用于“给定游戏名，快速复刻 Unity 核心体验”的多 Agent 并行流水线。

## 当前结构

- `agents/`: 可执行代理脚本
- `automation/`: 自动化入口脚本
- `docs/`: 已产出的文档与规则
- `projects/`: 每个游戏的执行目录（含模板）
- `archive/`: 归档历史产物

## 快速开始

1. 复制模板目录
2. 填写需求输入
3. 生成任务拆解
4. 并行执行 Code/Art
5. 人工测试收尾

## 新项目流程

1. 复制 `projects/_template` 为 `projects/<GameName>`
2. 编辑 `projects/<GameName>/spec/feature_input.json`
3. 依据 `docs/rules/AgentPool_Rules.md` 分配 Agent
4. 输出到 `projects/<GameName>/tasks/*` 与 `projects/<GameName>/assets/manifest/*`
5. 你执行人工测试并记录到 `projects/<GameName>/reports/`

## 关键规则入口

- 架构说明: `docs/architecture/GJ_Architecture.md`
- 通用拆解: `docs/architecture/Universal_Decomposition_Framework.md`
- 并行规则: `docs/rules/AgentPool_Rules.md`
- 自动驾驶: `docs/rules/Autopilot_Mode.md`
