# 多 Agent 并行规则（Unity 复刻）

## Agent 池

1. Planner: 机制拆解、任务编排、接口冻结
2. Gameplay: 角色、敌人、关卡核心循环
3. Systems: UI、存档、配置、数值管线
4. AssetOps: 资产清单、命名、占位填充
5. QA-Prep: 冒烟用例与回归清单

## 稳定通用模块（所有游戏都先按此拆）

1. 输入与控制（Input）
2. 核心循环（Core Loop）
3. 实体行为（Player/Enemy/NPC）
4. 进度与状态（Progress/Save）
5. UI 与反馈（HUD/Prompt/Effects）
6. 内容与资产映射（Asset Mapping）
7. 测试与诊断（Smoke/Regression/Debug）

说明：不同游戏只改变每个模块的复杂度，不改变模块骨架。

## 强制规则

1. 单文件单责任
同一时间只允许一个 Agent 写同一文件。

2. 先契约后并行
事件名、数据结构、目录命名在并行前冻结。

3. 明确写入边界
每个 Agent 必须声明“可写目录”和“禁止修改目录”。

4. 每日集成
每天至少一次主干集成和冒烟，避免最后合并爆炸。

5. 所有任务可验收
每条任务必须有 Done 条件，不允许“描述性完成”。

## 目录写权限建议

1. Planner: `projects/<GameName>/spec`, `projects/<GameName>/tasks`
2. Gameplay: Unity 工程 `Scripts/Gameplay`
3. Systems: Unity 工程 `Scripts/Systems`, `UI`
4. AssetOps: `projects/<GameName>/assets`
5. QA-Prep: `projects/<GameName>/reports`

## 任务卡最小字段

1. TaskID
2. Owner
3. Inputs
4. Outputs
5. Dependencies
6. DoneCriteria
7. Risk
8. EffortPoint (1-5)
9. OwnerShare (%)

## 禁止事项

1. 未冻结接口前开始跨模块实现
2. 直接改动他人写入边界内文件
3. 把“待讨论”当作“已完成”

## 分工倾向（帮手B加权）

1. 测试模块默认全归帮手B
2. 调试面板、日志采集、测试辅助脚本默认归帮手B
3. 只要不涉及主循环业务逻辑，优先把“工具层代码”分配给帮手B
