# Vampire Survivors M1 代码任务清单

## 阶段目标
实现最小可玩版本的核心循环

## 必须完成

### P0 核心系统（必须完成）
| 任务ID | 模块 | 任务描述 | 复杂度 | 预估h |
|--------|------|----------|--------|-------|
| CODE-M1-P0-01 | 项目骨架 | Unity项目初始化、目录结构搭建 | C1 | 1 |
| CODE-M1-P0-02 | 玩家控制 | WASD移动、边界限制、动画 | C2 | 2 |
| CODE-M1-P0-03 | 自动攻击 | 武器自动射击逻辑、目标选择 | C3 | 4 |
| CODE-M1-P0-04 | 投射物系统 | 子弹生成、移动、碰撞、对象池 | C3 | 3 |
| CODE-M1-P0-05 | 敌人生成 | 波次系统、敌人AI（追踪）、生成器 | C3 | 3 |
| CODE-M1-P0-06 | XP系统 | 宝石掉落、拾取、等级经验 | C2 | 2 |
| CODE-M1-P0-07 | 升级系统 | 升级面板、武器选择/强化 | C3 | 3 |
| CODE-M1-P0-08 | UI系统 | HP/XP条、分数、武器图标 | C2 | 2 |

### P1 扩展系统（尽量完成）
| 任务ID | 模块 | 任务描述 | 复杂度 | 预估h |
|--------|------|----------|--------|-------|
| CODE-M1-P1-01 | 武器系统 | 第2-3种武器实现 | C2 | 2 |
| CODE-M1-P1-02 | 敌人类型 | 增加1-2种敌人类型 | C2 | 2 |
| CODE-M1-P1-03 | 碰撞系统 | 敌人攻击判定、受伤反馈 | C2 | 2 |
| CODE-M1-P1-04 | 存档系统 | 本地存档（进度、解锁） | C2 | 1 |

---

## 执行顺序

### Day 1 上午
1. CODE-M1-P0-01 项目骨架
2. CODE-M1-P0-02 玩家控制

### Day 1 下午
3. CODE-M1-P0-03 自动攻击
4. CODE-M1-P0-04 投射物系统
5. 美术资源集成

### Day 1 晚上
6. CODE-M1-P0-05 敌人生成
7. CODE-M1-P0-06 XP系统
8. 打包给QA测试

### Day 2 上午
9. CODE-M1-P0-07 升级系统
10. CODE-M1-P0-08 UI系统
11. CODE-M1-P1-01~04 扩展功能

### Day 2 下午
12. 缺陷修复
13. 性能优化
14. 最终打包

---

## 接口规范

### 武器接口
```csharp
public interface IWeapon
{
    float Cooldown { get; }
    float Damage { get; }
    void Fire(Transform target);
}
```

### 敌人生成器接口
```csharp
public interface IEnemySpawner
{
    float SpawnInterval { get; set; }
    int MaxEnemies { get; set; }
    void StartSpawning();
    void StopSpawning();
}
```

### XP系统接口
```csharp
public interface IXPGem
{
    int Value { get; }
    void OnCollect();
}
```

---

## 依赖关系
- P0-02 依赖 P0-01
- P0-03 依赖 P0-02
- P0-04 依赖 P0-03
- P0-05 依赖 P0-02
- P0-06 依赖 P0-05
- P0-07 依赖 P0-06
- P0-08 依赖 P0-02, P0-06

---

## 交付物路径
- 代码: `Assets/Scripts/`
- 预设: `Assets/Prefabs/`
- 场景: `Assets/Scenes/`

## 交付给
- QA（你）：可运行构建包 + 变更说明
- Art（美术）：资源规格文档

## 验收标准
1. 可从主菜单进入游戏
2. 玩家可以移动并自动攻击
3. 敌人会生成并向玩家移动
4. 击杀敌人掉落XP
5. 升级可以选择武器
6. HP归零显示结束界面
