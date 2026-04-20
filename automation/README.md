# 游戏复刻自动化工具箱

## 目录结构

```
D:\GJ\automation\
├── README.md                    # 本文件
├── auto_pipeline.py             # 主流水线控制器
├── code_automation.py           # 代码自动化控制器
└── install_dependencies.py      # 依赖安装脚本
```

## 快速开始

### 1. 安装依赖
```powershell
cd D:\GJ\automation
pip install openai
```

### 2. 配置环境变量
```powershell
$env:OPENAI_API_KEY="your_api_key"
$env:OPENAI_BASE_URL="https://your-relay/v1"
```

### 3. 启动自动化
```powershell
# 完整流水线（分析+任务分解+代码自动化）
python auto_pipeline.py --game "游戏名" --milestone M1

# 仅代码自动化（如果任务包已生成）
python code_automation.py start --project 项目名 --game "游戏名"
```

## 命令参考

### auto_pipeline.py
| 命令 | 说明 |
|------|------|
| `--game "名称"` | 游戏名称 |
| `--milestone M1` | 里程碑（默认M1） |
| `--skip-agent` | 跳过AI，使用模板生成 |
| `--output-dir` | 输出目录 |

### code_automation.py
| 命令 | 说明 |
|------|------|
| `start --project X --game Y` | 启动代码自动化 |
| `status` | 查看状态和进度 |
| `board` | 查看任务看板 |
| `wait` | 等待所有任务完成 |

## 输出文件

| 文件 | 说明 |
|------|------|
| `D:\GJ\docs\dispatch\{game}_整体里程碑规划.md` | 里程碑规划 |
| `D:\GJ\docs\dispatch\{game}_{m}_美术任务清单.md` | 美术任务 |
| `D:\GJ\docs\dispatch\{game}_{m}_代码任务清单.md` | 代码任务 |
| `D:\GJ\docs\dispatch\{game}_{m}_测试任务清单.md` | 测试任务 |
| `D:\GJ\docs\dispatch\{game}_开源代码参考.md` | 代码参考 |
| `D:\GJ\docs\dispatch\{game}_Git协作策略.md` | Git协作 |
| `D:\GJ\game-projects\{project}\` | Unity项目代码 |

## 工作流程

```
┌────────────────────────────────────────────────────────────┐
│  auto_pipeline.py                                          │
│  ├── 游戏分析 (librarian)                                  │
│  ├── 任务分解 (dispatch)                                   │
│  └── 生成任务包 → dispatch/                                │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│  code_automation.py                                        │
│  ├── 加载任务队列                                          │
│  ├── 调度 deep agent 集群                                  │
│  └── 生成代码 → game-projects/                             │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│  Unity 构建                                                 │
│  └── 打包 exe → Builds/                                   │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│  人工检测                                                   │
│  └── 测试 → 反馈 → 修复循环                                 │
└────────────────────────────────────────────────────────────┘
```

## 用户视角

用户（总指挥）只需要：
1. 运行 `auto_pipeline.py`
2. 派发任务给队友
3. 测试构建包
4. 反馈问题

**零代码接触：用户不查看、不修改任何代码文件。**
