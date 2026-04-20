# Vampire Survivors 开源代码参考清单

## 项目目标
为2天Unity复刻项目提供可参考的开源实现

---

## 一、Vampire Survivors类型开源项目

### 1. Unity-Bullet-Hell
**链接**: https://github.com/jongallant/Unity-Bullet-Hell
**Stars**: ~500+
**用途**: 弹幕/投射物系统参考
**核心价值**:
- 高效的投射物管理方案
- 弹幕生成器模式
- 大量子弹渲染优化
**重点学习**:
- `BulletController.cs` - 投射物控制
- `BulletPool.cs` - 对象池实现
- 子弹轨迹算法

---

### 2. Danmokou
**链接**: https://github.com/Bagoum/danmokou
**Stars**: ~300+
**用途**: Unity弹幕引擎完整实现
**核心价值**:
- 模式驱动的弹幕设计
- 可扩展的技能系统
- 复杂的弹幕轨迹数学
**重点学习**:
- Pattern系统架构
- BulletManager实现
- 弹幕数据配置方式

---

### 3. Sentaur Survivors (Sentry Demo)
**链接**: https://github.com/sentry-demos/unity
**Stars**: ~200+
**用途**: Vampire Survivors风格克隆
**核心价值**:
- 完整的游戏结构
- 升级/波次系统
- 错误监控集成
**重点学习**:
- 项目目录结构
- 游戏循环设计
- 存档机制

---

### 4. Oskar-Norberg/Vampire-Survivors-Clone
**链接**: https://github.com/Oskar-Norberg/Vampire-Survivors-Clone
**Stars**: ~100+
**用途**: 完整的VS风格实现
**核心价值**:
- 武器升级系统
- 敌人AI实现
- UI/UX设计
**重点学习**:
- `WeaponSystem.cs`
- `EnemyController.cs`
- `UpgradePanel.cs`

---

### 5. matthiasbroske/VampireSurvivorsClone
**链接**: https://github.com/matthiasbroske/VampireSurvivorsClone
**Stars**: ~50+
**用途**: 移动端/PC通用实现
**核心价值**:
- 对象池实战
- 性能优化
- 武器进化系统
**重点学习**:
- 对象池管理
- 进化条件逻辑
- 敌人生成调度

---

### 6. michalbilik/ZTI-survivors
**链接**: https://github.com/michalbilik/ZTI-survivors
**Stars**: ~30+
**用途**: 简洁实现版本
**核心价值**:
- 清晰的代码结构
- 基础功能完整
- 易于学习
**重点学习**:
- 整体架构
- 核心脚本命名

---

### 7-9. 其他克隆项目
- `VampAK1864/Vampire-Survivors`
- `GamerXWarrior/Vampire_Survivors`
- `strongvu/VampireSurvivors`

**用途**: 对比不同实现方式，寻找最佳实践

---

## 二、Unity 2D最佳实践项目

### Unity官方示例
**2D Game Kit**: https://unity.com/features/2d-gamekit
**用途**: Unity官方2D游戏开发套件
**包含**:
- 角色控制器
- 敌人AI模板
- 关卡设计工具
- 战斗系统

**Top-Down Shooter Sample**: Unity Package Manager直接导入
```
Window > Package Manager > Samples > 2D Sample Game Series
```

---

## 三、核心参考模块

### 1. 对象池系统
**参考**: Unity-Bullet-Hell, matthiasbroske
```
必读文件:
- ObjectPool.cs
- PooledObject.cs
- BulletPool.cs
```
**实现要点**:
```csharp
public class ObjectPool<T> where T : PooledObject
{
    private Queue<T> available = new Queue<T>();
    private T prefab;
    
    public T Get() { ... }
    public void Release(T obj) { ... }
}
```

---

### 2. 自动攻击系统
**参考**: Oskar-Norberg, Sentaur
```
必读文件:
- WeaponSystem.cs
- AutoAttackController.cs
- WeaponData.cs
```
**实现要点**:
```csharp
public class AutoAttackController : MonoBehaviour
{
    [SerializeField] private float attackRange = 5f;
    [SerializeField] private float attackCooldown = 1f;
    
    private float lastAttackTime;
    
    void Update()
    {
        if (Time.time - lastAttackTime >= attackCooldown)
        {
            var target = FindNearestEnemy();
            if (target != null && InRange(target))
            {
                Attack(target);
                lastAttackTime = Time.time;
            }
        }
    }
}
```

---

### 3. 波次/敌人生成系统
**参考**: Sentaur, matthiasbroske
```
必读文件:
- WaveManager.cs
- EnemySpawner.cs
- EnemyData.cs
```
**实现要点**:
```csharp
public class WaveManager : MonoBehaviour
{
    public float spawnInterval = 2f;
    public int maxEnemies = 30;
    private float elapsedTime;
    
    void Update()
    {
        elapsedTime += Time.deltaTime;
        float currentInterval = Mathf.Max(0.5f, spawnInterval - elapsedTime * 0.01f);
        
        if (Time.time >= nextSpawnTime && currentEnemyCount < maxEnemies)
        {
            SpawnEnemy();
        }
    }
}
```

---

### 4. XP/升级系统
**参考**: Oskar-Norberg
```
必读文件:
- XPManager.cs
- LevelUpUI.cs
- UpgradeData.cs
```
**实现要点**:
```csharp
public class LevelUpSystem : MonoBehaviour
{
    public int currentLevel = 1;
    public int currentXP = 0;
    public int xpToNextLevel;
    
    public void AddXP(int amount)
    {
        currentXP += amount;
        if (currentXP >= xpToNextLevel)
        {
            LevelUp();
        }
    }
    
    void LevelUp()
    {
        currentLevel++;
        ShowLevelUpUI();
    }
}
```

---

## 四、项目结构参考

```
Assets/
├── Scripts/
│   ├── Core/
│   │   ├── GameManager.cs
│   │   ├── TimeManager.cs
│   │   └── EventBus.cs
│   ├── Player/
│   │   ├── PlayerController.cs
│   │   ├── PlayerStats.cs
│   │   └── AutoAttackController.cs
│   ├── Weapons/
│   │   ├── WeaponBase.cs
│   │   ├── WeaponWhip.cs
│   │   ├── WeaponFire.cs
│   │   └── WeaponData.cs
│   ├── Enemies/
│   │   ├── EnemyBase.cs
│   │   ├── EnemyAI.cs
│   │   ├── EnemySpawner.cs
│   │   └── WaveManager.cs
│   ├── Collectibles/
│   │   ├── XPGem.cs
│   │   └── Coin.cs
│   ├── UI/
│   │   ├── HUD.cs
│   │   ├── LevelUpUI.cs
│   │   └── GameOverUI.cs
│   ├── Pool/
│   │   ├── ObjectPool.cs
│   │   └── PooledObject.cs
│   └── Data/
│       ├── GameData.cs
│       └── SaveManager.cs
├── Prefabs/
│   ├── Player.prefab
│   ├── Enemies/
│   ├── Projectiles/
│   └── UI/
├── ScriptableObjects/
│   ├── WeaponDatas/
│   ├── EnemyDatas/
│   └── LevelData/
├── Scenes/
│   ├── MainMenu.unity
│   └── Game.unity
└── Art/
    ├── Sprites/
    └── Effects/
```

---

## 五、学习优先级建议

### 第一优先级（必读）
1. **Unity-Bullet-Hell** - 对象池 + 投射物
2. **Oskar-Norberg** - 武器系统 + 升级UI
3. **Sentaur** - 整体架构 + 波次系统

### 第二优先级（选读）
4. **Danmokou** - 弹幕模式设计
5. **matthiasbroske** - 进化系统

### 第三优先级（补充）
6. Unity 2D Game Kit - Unity原生方案

---

## 六、快速落地建议

### 克隆建议
```bash
# 克隆最相关的参考项目
git clone https://github.com/Oskar-Norberg/Vampire-Survivors-Clone.git ReferenceProjects/VS-Clone
git clone https://github.com/jongallant/Unity-Bullet-Hell.git ReferenceProjects/BulletHell
```

### 使用方式
1. 打开参考项目，Play场景测试
2. 复制核心脚本到你的项目
3. 按你的命名规范重命名
4. 适配你的数据结构和接口
5. 删除参考项目的额外依赖

### 注意事项
- 参考代码可能有不同许可证，商用需注意
- 建议学习思路，不直接复制全部代码
- 保持代码风格一致性
