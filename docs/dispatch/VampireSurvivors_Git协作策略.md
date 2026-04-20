# Vampire Survivors Git协作策略

## 团队成员
| 角色 | 职责 | Git用户名 |
|------|------|-----------|
| 总指挥+代码 | 项目架构、核心代码、最终打包 | (你) |
| 美术 | 美术资源、视觉效果 | (队友A) |
| 测试 | 冒烟测试、缺陷报告 | (队友B) |

---

## 一、仓库结构

```
vampire-survivors-clone/
├── .git/
├── Assets/                    # Unity资源（主分支）
│   ├── Scripts/               # 代码（总指挥维护）
│   ├── Art/                   # 美术资源（美术维护）
│   └── QA/                    # 测试报告
├── Builds/                    # 构建产物（不提交大文件）
├── Docs/                      # 文档（全员可写）
│   └── dispatch/              # 任务派发文档
├── Reference/                # 参考项目（可选）
└── .gitignore
```

---

## 二、分支策略

### 分支命名规范
```
[类型]-[角色]-[功能]

示例:
main                        # 主分支，稳定可运行
code-skeleton               # 代码：项目骨架
code-player                 # 代码：玩家控制
code-weapon                 # 代码：武器系统
code-enemy                  # 代码：敌人生成
code-ui                     # 代码：UI系统
art-assets-v1               # 美术：资源包v1
art-assets-v2               # 美术：资源包v2
test-report-m1              # 测试：M1测试报告
```

### 分支类型
| 前缀 | 维护者 | 用途 |
|------|--------|------|
| `code-` | 总指挥 | 代码功能开发 |
| `art-` | 美术 | 美术资源提交 |
| `test-` | 测试 | 测试报告存档 |
| `hotfix-` | 总指挥 | 紧急修复 |

---

## 三、协作流程

### 每日工作流

```
┌─────────────────────────────────────────────────────────────┐
│                      早上：同步 + 分配                       │
├─────────────────────────────────────────────────────────────┤
│  1. 总指挥 pull main                                        │
│  2. 查看昨日构建状态                                         │
│  3. 在群里分配今日任务                                        │
│  4. 各自创建功能分支                                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      白天：各自开发                           │
├─────────────────────────────────────────────────────────────┤
│  总指挥: 代码开发 → 频繁push代码分支                          │
│  美术:   资源制作 → 完成一批资源 → 提交art分支                 │
│  测试:   准备用例 → 等待构建包 → 执行测试                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      晚上：集成 + 构建                        │
├─────────────────────────────────────────────────────────────┤
│  1. 总指挥 merge代码到main                                   │
│  2. 美术 merge资源到main                                     │
│  3. 构建新包                                                 │
│  4. 测试取包，执行测试                                        │
│  5. 提交缺陷报告                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 四、具体命令

### 总指挥（代码）

```powershell
# 1. 早上同步
git checkout main
git pull origin main

# 2. 创建代码分支
git checkout -b code-weapon-system

# 3. 开发中频繁保存（建议每2小时）
git add .
git commit -m "feat: 实现武器基础类"
git push origin code-weapon-system

# 4. 晚上合并到main
git checkout main
git merge code-weapon-system
git push origin main

# 5. 打构建包
# Unity菜单: File > Build Settings > Build
# 输出到 Builds/M1_v0.1.20241015/
```

### 美术（队友）

```powershell
# 1. 早上同步
git checkout main
git pull origin main

# 2. 创建资源分支
git checkout -b art-assets-v1

# 3. 添加资源
# 将完成的资源放进 Assets/Art/ 目录

# 4. 提交
git add Assets/Art/
git commit -m "art: 添加角色和敌人精灵图"
git push origin art-assets-v1

# 5. 通知总指挥合并
# (在群里@总指挥："资源包v1已提交，可以合并了")
```

### 测试（队友）

```powershell
# 测试不需要合并代码，只需下载最新构建

# 1. 克隆仓库（首次）
git clone https://github.com/yourusername/vampire-survivors-clone.git
cd vampire-survivors-clone

# 2. 每天获取最新构建
git checkout main
git pull origin main
# 从群里下载最新的Build包，或从固定共享位置复制

# 3. 测试后提交报告
git checkout -b test-report-m1
# 创建测试报告文档到 Docs/QA/
git add Docs/QA/
git commit -m "test: M1冒烟测试报告"
git push origin test-report-m1
```

---

## 五、冲突处理

### 代码冲突（总指挥处理）

```powershell
# 如果合并时冲突
git checkout main
git pull
git checkout -b code-weapon

# 尝试合并
git merge main
# 出现冲突，手动解决

# 解决后
git add .
git commit -m "merge: 解决与main的冲突"
git push origin code-weapon
```

### 资源冲突（美术 + 总指挥协商）

```powershell
# 如果美术和代码改了同一文件
# 1. 美术通知总指挥
# 2. 总指挥决定保留哪个版本
# 3. 总指挥执行合并
```

### 冲突预防规则
1. **美术资源文件夹**只有美术可以修改
2. **代码文件夹**只有总指挥可以修改
3. **共享文件夹**（如配置表）修改前先沟通
4. **不要直接改main分支**

---

## 六、标签和版本

### 每日构建标签

```powershell
# 每天构建后打标签
git tag -a v0.1.Day1 -m "Day1构建：核心循环可用"
git push origin v0.1.Day1

git tag -a v0.2.Day2 -m "Day2构建：完整M1"
git push origin v0.2.Day2
```

### 版本命名
```
v[主版本].[特性版本].[日期/序号]

示例:
v0.1.Day1    # M1第一天构建
v0.2.Day2    # M1第二天构建
v1.0.M1      # M1完成
```

---

## 七、GitHub仓库创建（总指挥执行）

```powershell
# 1. 在GitHub创建仓库
# Settings > New repository
# 名称: vampire-survivors-clone

# 2. 本地初始化
cd vampire-survivors-clone
git init
git add .
git commit -m "chore: 初始化Unity项目"

# 3. 关联远程
git remote add origin https://github.com/yourusername/vampire-survivors-clone.git

# 4. 首次推送
git push -u origin main

# 5. 邀请队友
# GitHub > Settings > Collaborators > Add people
```

---

## 八、共享方式（备选：不用Git的情况）

如果队友不会用Git，用网盘共享：

```
共享文件夹/
├── 00_Code/              # 总指挥放代码zip
├── 01_Art/               # 美术放资源包
├── 02_Builds/            # 总指挥放构建包
└── 03_QA_Reports/       # 测试放报告
```

**规则**:
- 文件命名: `[角色]_[功能]_[日期].zip`
- 覆盖前先备份旧版本
- 群里通知更新

---

## 九、Checklist

### 总指挥
- [ ] 创建GitHub仓库
- [ ] 设置 .gitignore
- [ ] 邀请队友
- [ ] 每天合并代码
- [ ] 每天打构建包
- [ ] 群里通知构建更新

### 美术
- [ ] 接受邀请 / 克隆仓库
- [ ] 创建 art-assets 分支
- [ ] 资源完成后提交
- [ ] 群里通知

### 测试
- [ ] 克隆仓库
- [ ] 熟悉测试用例文档
- [ ] 等待构建包
- [ ] 执行测试
- [ ] 提交报告

---

## 十、每日沟通模板

### 早上群消息
```
📅 Day 1 早上
总指挥: 
- 今日代码任务: 玩家控制 + 自动攻击
- 美术: 完成角色精灵图
- 测试: 准备冒烟用例
- 构建包预计: 18:00
```

### 晚上群消息
```
📦 Day 1 构建包
版本: v0.1.Day1
路径: Builds/M1_v0.1.Day1/
更新:
- ✅ 玩家移动
- ✅ 自动攻击
- ⏳ XP系统(开发中)
- ⏳ 升级系统(开发中)
测试: @队友B 可以开始冒烟
```
