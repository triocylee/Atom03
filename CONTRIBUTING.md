# Contributing Guide

本仓库采用 1 天冲刺 + Gate 验收模式。

## 0. 先读规则

1. `docs/rules/Autopilot_Mode.md`
2. `docs/rules/AgentPool_Rules.md`
3. `docs/architecture/Universal_Decomposition_Framework.md`

## 1. 分工与写入边界

1. Owner（triocylee）
- 负责拆解、接口冻结、核心代码

2. Helper A
- 负责资产清单、占位资产、UI/表现层接线

3. Helper B
- 负责测试、回归闭环、工具层和调试脚本

禁止跨写入边界直接改文件；如需跨边界，先在 PR 说明理由。

## 2. 任务与分支命名

1. 每个任务必须有 `TaskID`（如 `C-004`、`A-002`、`Q-003`）
2. 分支命名：
- `task/C-004-inventory`
- `task/A-002-resource-nodes`
- `task/Q-001-smoke`

## 3. 提交流程

1. 从 `main` 拉最新
2. 建分支并提交最小可审查变更
3. 开 PR 到 `main`
4. 通过审查后合并

## 4. PR 必须包含

1. 关联 `TaskID`
2. 变更范围与写入目录
3. 验收结果（对应 Gate）
4. 风险与回滚点

## 5. Gate 规则

1. Gate A：需求冻结 + `WORKLOAD_CHECK`
2. Gate B：核心切片可跑通
3. Gate C：资产映射可追踪
4. Gate D：集成与冒烟通过

除阻塞问题外，不在 Gate 外打断主流程。
