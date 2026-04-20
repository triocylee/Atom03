"""
代码自动化控制器 - 零代码接触版

功能:
- 管理deep agent集群并行生成代码
- 用户只看到进度和最终构建
- 不暴露代码细节

用法:
    python code_automation.py --project "VampireSurvivors" --milestone M1
"""

import argparse
import os
import subprocess
import json
import time
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

# ============== 配置 ==============
DEFAULT_PROJECT_DIR = r"D:\GJ\game-projects"
TASK_QUEUE_FILE = r"D:\GJ\docs\dispatch\task_queue.json"
PROGRESS_FILE = r"D:\GJ\docs\dispatch\code_progress.json"

# ============== 颜色输出 ==============
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    DIM = '\033[2m'

def log(msg, level="INFO"):
    colors = {"INFO": Colors.CYAN, "OK": Colors.GREEN, "WARN": Colors.YELLOW, "ERROR": Colors.RED, "PROGRESS": Colors.BLUE}
    prefix = {"INFO": "ℹ", "OK": "✓", "WARN": "⚠", "ERROR": "✗", "PROGRESS": "→"}
    print(f"{colors.get(level, Colors.CYAN)}[{datetime.now().strftime('%H:%M:%S')}] {prefix.get(level, 'ℹ')} {msg}{Colors.ENDC}")

# ============== 数据结构 ==============
@dataclass
class CodeTask:
    task_id: str
    module: str
    description: str
    priority: str  # P0, P1
    estimated_hours: float
    status: str = "pending"  # pending, doing, done, blocked
    agent_session: Optional[str] = None
    depends_on: List[str] = None
    
    def __post_init__(self):
        if self.depends_on is None:
            self.depends_on = []

@dataclass
class BuildStatus:
    version: str
    status: str  # building, success, failed
    progress: int  # 0-100
    changelog: List[str] = None
    download_url: Optional[str] = None
    
    def __post_init__(self):
        if self.changelog is None:
            self.changelog = []

# ============== 任务队列 ==============
def load_tasks(game_name: str) -> List[CodeTask]:
    """从dispatch文档加载代码任务"""
    task_file = Path(TASK_QUEUE_FILE)
    
    if task_file.exists():
        with open(task_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [CodeTask(**t) for t in data]
    
    # 默认任务列表（从M1代码任务清单）
    return [
        CodeTask(
            task_id="CODE-M1-P0-01",
            module="项目骨架",
            description="Unity项目初始化、目录结构搭建",
            priority="P0",
            estimated_hours=1
        ),
        CodeTask(
            task_id="CODE-M1-P0-02",
            module="玩家控制",
            description="WASD移动、边界限制、动画",
            priority="P0",
            estimated_hours=2,
            depends_on=["CODE-M1-P0-01"]
        ),
        CodeTask(
            task_id="CODE-M1-P0-03",
            module="自动攻击",
            description="武器自动射击逻辑、目标选择",
            priority="P0",
            estimated_hours=4,
            depends_on=["CODE-M1-P0-02"]
        ),
        CodeTask(
            task_id="CODE-M1-P0-04",
            module="投射物系统",
            description="子弹生成、移动、碰撞、对象池",
            priority="P0",
            estimated_hours=3,
            depends_on=["CODE-M1-P0-03"]
        ),
        CodeTask(
            task_id="CODE-M1-P0-05",
            module="敌人生成",
            description="波次系统、敌人AI、生成器",
            priority="P0",
            estimated_hours=3,
            depends_on=["CODE-M1-P0-02"]
        ),
        CodeTask(
            task_id="CODE-M1-P0-06",
            module="XP系统",
            description="宝石掉落、拾取、等级经验",
            priority="P0",
            estimated_hours=2,
            depends_on=["CODE-M1-P0-05"]
        ),
        CodeTask(
            task_id="CODE-M1-P0-07",
            module="升级系统",
            description="升级面板、武器选择/强化",
            priority="P0",
            estimated_hours=3,
            depends_on=["CODE-M1-P0-06"]
        ),
        CodeTask(
            task_id="CODE-M1-P0-08",
            module="UI系统",
            description="HP/XP条、分数、武器图标",
            priority="P0",
            estimated_hours=2,
            depends_on=["CODE-M1-P0-02", "CODE-M1-P0-06"]
        ),
        CodeTask(
            task_id="CODE-M1-P1-01",
            module="武器扩展",
            description="第2-3种武器实现",
            priority="P1",
            estimated_hours=2,
            depends_on=["CODE-M1-P0-04"]
        ),
        CodeTask(
            task_id="CODE-M1-P1-02",
            module="敌人类型",
            description="增加1-2种敌人类型",
            priority="P1",
            estimated_hours=2,
            depends_on=["CODE-M1-P0-05"]
        ),
    ]

def save_progress(tasks: List[CodeTask]):
    """保存进度"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump([{
            "task_id": t.task_id,
            "module": t.module,
            "description": t.description,
            "priority": t.priority,
            "estimated_hours": t.estimated_hours,
            "status": t.status,
            "depends_on": t.depends_on
        } for t in tasks], f, ensure_ascii=False, indent=2)

# ============== Agent调度 ==============
def spawn_code_agent(task: CodeTask, project_dir: str, game_name: str) -> str:
    """启动一个deep agent来执行代码任务"""
    log(f"启动Agent: {task.module}", "PROGRESS")
    
    # 构建prompt给deep agent
    prompt = f"""## 任务: 实现Unity游戏模块

### 游戏名: {game_name}
### 模块: {task.module}
### 描述: {task.description}
### 任务ID: {task.task_id}

### 项目路径: {project_dir}

### 要求:
1. 在 Assets/Scripts/ 下创建相应的C#脚本
2. 使用Unity最佳实践（MonoBehaviour, SerializeField等）
3. 遵循命名规范
4. 包含必要的using语句
5. 添加XML注释
6. 代码要完整可运行，不要占位符

### 输出:
- 创建的所有文件路径
- 简要说明实现的功能
- 如有依赖外部资源，说明需要的资源规格

### 重要:
- 不要解释你在做什么，直接生成代码
- 代码文件保存到 {project_dir}/Assets/Scripts/
"""
    
    # 这里会调用实际的deep agent
    # 返回session_id用于跟踪
    return f"agent_{task.task_id}"

def check_agent_result(session_id: str) -> bool:
    """检查Agent执行结果"""
    # 实际实现中会调用background_output
    # 这里简化返回True
    return True

# ============== 进度展示 ==============
def show_task_board(tasks: List[CodeTask]):
    """显示任务看板（用户视角）"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}📋 代码任务看板{Colors.ENDC}")
    print(f"{Colors.BLUE}{'='*60}{Colors.ENDC}\n")
    
    # 按状态分组
    pending = [t for t in tasks if t.status == "pending"]
    doing = [t for t in tasks if t.status == "doing"]
    done = [t for t in tasks if t.status == "done"]
    blocked = [t for t in tasks if t.status == "blocked"]
    
    # 进度条
    total = len(tasks)
    done_count = len(done)
    progress = int(100 * done_count / total) if total > 0 else 0
    bar_len = 20
    filled = int(bar_len * done_count / total) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_len - filled)
    
    print(f"  进度: [{bar}] {progress}% ({done_count}/{total})")
    print()
    
    # P0任务详情
    print(f"  {Colors.GREEN}✓{Colors.ENDC} 已完成 ({len(done)})")
    for t in done:
        print(f"    {Colors.DIM}{t.module}: {t.description[:30]}...{Colors.ENDC}")
    
    print(f"\n  {Colors.CYAN}→{Colors.ENDC} 进行中 ({len(doing)})")
    for t in doing:
        print(f"    {Colors.CYAN}{t.module}: {t.description[:30]}...{Colors.ENDC}")
    
    print(f"\n  {Colors.YELLOW}○{Colors.ENDC} 等待中 ({len(pending)})")
    for t in pending[:5]:  # 只显示前5个
        print(f"    {t.module}")
    if len(pending) > 5:
        print(f"    {Colors.DIM}...还有{len(pending)-5}个{Colors.ENDC}")
    
    if blocked:
        print(f"\n  {Colors.RED}✗{Colors.ENDC} 阻塞 ({len(blocked)})")
        for t in blocked:
            print(f"    {t.module}: 等待 {t.depends_on}")
    
    print()

def show_build_status():
    """显示构建状态（用户视角）"""
    build_file = Path(PROGRESS_FILE).parent / "build_status.json"
    
    if build_file.exists():
        with open(build_file, 'r', encoding='utf-8') as f:
            status = json.load(f)
        
        print(f"\n{Colors.GREEN}{'='*60}{Colors.ENDC}")
        print(f"{Colors.GOLD}📦 构建状态{Colors.ENDC}")
        print(f"{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
        print(f"  版本: {status.get('version', 'N/A')}")
        print(f"  状态: {status.get('status', 'unknown')}")
        print(f"  进度: {status.get('progress', 0)}%")
        if status.get('download_url'):
            print(f"  下载: {status['download_url']}")
        print()

# ============== 主命令 ==============
def cmd_start(project_name: str, game_name: str):
    """启动代码自动化"""
    project_dir = Path(DEFAULT_PROJECT_DIR) / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建Unity项目结构
    unity_structure = [
        "Assets/Scripts/Core",
        "Assets/Scripts/Player",
        "Assets/Scripts/Weapons",
        "Assets/Scripts/Enemies",
        "Assets/Scripts/UI",
        "Assets/Scripts/Pool",
        "Assets/Scripts/Data",
        "Assets/Prefabs",
        "Assets/Scenes",
        "Assets/Art",
        "Builds",
    ]
    
    for folder in unity_structure:
        (project_dir / folder).mkdir(parents=True, exist_ok=True)
    
    log(f"项目目录已创建: {project_dir}", "OK")
    
    # 加载任务
    tasks = load_tasks(game_name)
    
    # 识别可立即执行的任务（无依赖）
    ready_tasks = [t for t in tasks if t.status == "pending" and not t.depends_on]
    
    log(f"开始执行 {len(ready_tasks)} 个并行任务...", "PROGRESS")
    
    # 启动并行Agent
    agent_sessions = []
    for task in ready_tasks:
        session = spawn_code_agent(task, str(project_dir), game_name)
        task.status = "doing"
        task.agent_session = session
        agent_sessions.append(session)
    
    save_progress(tasks)
    
    print(f"\n{Colors.GREEN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.GREEN}🚀 代码自动化已启动{Colors.ENDC}")
    print(f"{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
    print(f"  并行运行: {len(ready_tasks)} 个Agent")
    print(f"  项目路径: {project_dir}")
    print(f"\n  使用 'python code_automation.py status' 查看进度")
    print(f"  使用 'python code_automation.py board' 查看任务看板\n")

def cmd_status():
    """查看状态"""
    tasks = load_tasks("")
    show_task_board(tasks)
    show_build_status()

def cmd_board():
    """查看任务看板"""
    tasks = load_tasks("")
    show_task_board(tasks)

def cmd_wait():
    """等待所有任务完成"""
    log("等待Agent完成...", "PROGRESS")
    
    while True:
        tasks = load_tasks("")
        pending = [t for t in tasks if t.status in ["pending", "doing"]]
        
        if not pending:
            log("所有任务完成！", "OK")
            break
        
        show_task_board(tasks)
        time.sleep(30)  # 30秒检查一次

def main():
    parser = argparse.ArgumentParser(description="代码自动化控制器")
    subparsers = parser.add_subparsers(dest="cmd", help="命令")
    
    # start命令
    start_parser = subparsers.add_parser("start", help="启动代码自动化")
    start_parser.add_argument("--project", required=True, help="项目名称")
    start_parser.add_argument("--game", required=True, help="游戏名称")
    
    # status命令
    subparsers.add_parser("status", help="查看状态")
    
    # board命令
    subparsers.add_parser("board", help="查看任务看板")
    
    # wait命令
    subparsers.add_parser("wait", help="等待完成")
    
    args = parser.parse_args()
    
    if args.cmd == "start":
        cmd_start(args.project, args.game)
    elif args.cmd == "status":
        cmd_status()
    elif args.cmd == "board":
        cmd_board()
    elif args.cmd == "wait":
        cmd_wait()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
