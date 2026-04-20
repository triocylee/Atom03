# Vampire Survivors M1 美术任务清单

## 阶段目标
为M1阶段提供基础美术资源，确保代码可以正常集成和测试

## 必须完成
1. 占位符美术资源（代码优先）
2. 基础角色/敌人精灵图
3. UI元素资源
4. 简单特效（命中/死亡）

---

## 资源规格表

### 角色资源
| 资源名 | 类型 | 尺寸 | 格式 | 数量 | 命名规范 |
|--------|------|------|------|------|----------|
| Player | Sprite | 64x64 | PNG | 4方向各1 | player_idle_N.png |
| Player_Attack | Sprite | 64x64 | PNG | 1 | player_attack.png |

### 敌人资源
| 资源名 | 类型 | 尺寸 | 格式 | 数量 | 命名规范 |
|--------|------|------|------|------|----------|
| Enemy_Basic | Sprite | 32x32 | PNG | 3 | enemy_basic_1.png |
| Enemy_Fast | Sprite | 32x32 | PNG | 2 | enemy_fast_1.png |

### 武器/投射物
| 资源名 | 类型 | 尺寸 | 格式 | 数量 | 命名规范 |
|--------|------|------|------|------|----------|
| Bullet_Whip | Sprite | 16x16 | PNG | 3 | bullet_whip_1.png |
| Bullet_Fire | Sprite | 8x8 | PNG | 3 | bullet_fire_1.png |

### UI资源
| 资源名 | 类型 | 尺寸 | 格式 | 数量 | 命名规范 |
|--------|------|------|------|------|----------|
| HP_Bar | Sprite | 200x20 | PNG | 1 | ui_hp_bar.png |
| XP_Bar | Sprite | 200x20 | PNG | 1 | ui_xp_bar.png |
| Icon_Coin | Sprite | 32x32 | PNG | 1 | ui_icon_coin.png |
| Icon_Level | Sprite | 32x32 | PNG | 1 | ui_icon_level.png |

### 特效资源
| 资源名 | 类型 | 尺寸 | 格式 | 数量 | 命名规范 |
|--------|------|------|------|------|----------|
| Hit_Effect | SpriteSheet | 64x64 | PNG | 4帧 | fx_hit_1~4.png |
| Death_Effect | SpriteSheet | 64x64 | PNG | 6帧 | fx_death_1~6.png |
| XP_Gem | Sprite | 16x16 | PNG | 3 | xp_gem_1.png |

---

## 交付物格式
所有资源放在 `Assets/Art/` 目录下：
```
Assets/Art/
├── Sprites/
│   ├── Characters/
│   ├── Enemies/
│   ├── Projectiles/
│   └── UI/
├── Effects/
└── Materials/
```

## 命名规范
- 全部小写，下划线分隔
- 格式：[类型]_[名称]_[序号].png
- 序号从1开始

## 交付给
- Code（你）：资源文件 + 规格说明文档
- QA（队友）：资源截图用于测试验收

## 开始条件
- 无前置依赖，可以立即开始

## 验收标准
1. 代码可以正常加载所有精灵图
2. 精灵图尺寸符合规格表
3. 命名符合规范
