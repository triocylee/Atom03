# Rust Core Experience - QA Tasks

## Stage Goal

为你人工测试提供可执行清单，确保核心闭环可验证。

## Smoke Checklist

1. 新档进入后 3 分钟内可完成首次采集
2. 采集后可打开背包并看到资源堆叠
3. 可制作至少 1 件工具并加入快捷栏
4. 可成功放置地基+墙+门形成最小掩体
5. 夜晚可触发基础 AI 攻击并可击杀
6. 死亡后重生逻辑符合配置
7. 保存后重进可恢复关键状态

## Regression Scope

1. 资源节点刷新与掉落概率
2. 背包拖拽与快捷栏绑定
3. 建造碰撞合法性检测
4. 生存指标衰减和扣血阈值
5. AI 仇恨切换与寻路稳定性

## Bug Ticket Format

1. `ID`: `BUG-YYYYMMDD-XXX`
2. `Build`: 提交号/日期
3. `Steps`: 最小复现步骤
4. `Expected`: 预期行为
5. `Actual`: 实际行为
6. `Severity`: S1-S4
7. `Owner`: Gameplay/Systems/AssetOps

## Blocker Definition

1. 任何导致主循环中断或进度丢失的问题定义为阻塞
2. 任意 15 分钟必现崩溃定义为阻塞
