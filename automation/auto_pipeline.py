"""
游戏复刻自动化流水线 - 主控制器

用法:
    python auto_pipeline.py --game "游戏名" --milestone M1

流程:
    1. 游戏分析 (librarian)
    2. 生成三角色任务包 (dispatch agent)
    3. 启动代码自动化 (deep agent集群)
    4. 构建打包 (最终人工检测)
"""

import argparse
import os
import subprocess
import time
from pathlib import Path
from datetime import datetime

# ============== 配置 ==============
DEFAULT_OUTPUT_DIR = r"D:\GJ\docs\dispatch"
DEFAULT_CODE_DIR = r"D:\GJ\game-projects"
GITHUB_BASE = "https://github.com"  # 替换为你的GitHub用户名

# ============== 颜色输出 ==============
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log_step(step, status="INFO"):
    colors = {"INFO": Colors.CYAN, "OK": Colors.GREEN, "WARN": Colors.YELLOW, "ERROR": Colors.RED}
    print(f"{colors.get(status, Colors.CYAN)}[{datetime.now().strftime('%H:%M:%S')}] {step}{Colors.ENDC}")

def log_user_action(msg):
    print(f"\n{Colors.YELLOW}{'='*50}{Colors.ENDC}")
    print(f"{Colors.YELLOW}👤 用户操作: {msg}{Colors.ENDC}")
    print(f"{Colors.YELLOW}{'='*50}{Colors.ENDC}\n")

# ============== 步骤定义 ==============
STEPS = [
    {
        "id": 1,
        "name": "游戏分析",
        "description": "使用librarian分析游戏核心玩法、技术特点",
        "auto": True,
        "agent": "librarian",
        "output": "游戏分析报告.md",
    },
    {
        "id": 2,
        "name": "开源代码参考",
        "description": "查找Unity项目结构和参考实现",
        "auto": True,
        "agent": "explore",
        "output": "开源代码参考.md",
    },
    {
        "id": 3,
        "name": "生成任务包",
        "description": "生成美术/代码/测试三角色任务清单",
        "auto": True,
        "agent": "dispatch",
        "output": "{game}_{milestone}_*_任务清单.md",
    },
    {
        "id": 4,
        "name": "派发任务",
        "description": "人工派发美术和测试任务给队友",
        "auto": False,
        "user_action": "发送文档给队友",
    },
    {
        "id": 5,
        "name": "代码自动化制作",
        "description": "使用deep agent集群自动编写代码",
        "auto": True,
        "agent": "deep",
        "output": "Assets/Scripts/",
    },
    {
        "id": 6,
        "name": "构建打包",
        "description": "Unity构建exe",
        "auto": False,
        "user_action": "Unity手动打包",
    },
    {
        "id": 7,
        "name": "人工检测",
        "description": "运行exe，测试核心功能",
        "auto": False,
        "user_action": "测试并反馈问题",
    },
]

# ============== 自动化执行 ==============
def run_dispatch_agent(game_name: str, milestone: str, base_url: str, api_key: str):
    """运行dispatch agent生成任务包"""
    log_step("启动dispatch agent...", "INFO")
    
    agent_path = r"D:\GJ\agents\game_replica_dispatch"
    cmd = [
        "python", "run_agent.py",
        "--game", game_name,
        "--milestone", milestone,
        "--base-url", base_url,
        "--api-key", api_key,
    ]
    
    result = subprocess.run(cmd, cwd=agent_path, capture_output=True, text=True)
    
    if result.returncode == 0:
        log_step("任务包生成完成", "OK")
        return True
    else:
        log_step(f"任务包生成失败: {result.stderr}", "ERROR")
        return False

def generate_dispatch_docs_manually(game_name: str, milestone: str, output_dir: str):
    """手动生成dispatch文档（当agent不可用时）"""
    log_step("手动生成dispatch文档...", "INFO")
    
    docs = {
        f"{game_name}_整体里程碑规划.md": f"# {game_name} 整体里程碑规划\n\n## 项目目标\n2天内完成核心体验版复刻。\n\n## 核心玩法循环\n1. 玩家移动\n2. 自动攻击\n3. 击杀敌人\n4. XP升级\n5. 存活波次\n\n## 里程碑\n- M1: Skeleton runnable\n- M2: Core loop stable\n- M3: Content reinforcement\n- M4: Polish\n",
        f"{game_name}_{milestone}_美术任务清单.md": f"# {game_name} M1 美术任务清单\n\n## 阶段目标\n提供基础美术资源\n\n## 资源清单\n- 角色精灵\n- 敌人精灵\n- UI元素\n- 特效\n",
        f"{game_name}_{milestone}_代码任务清单.md": f"# {game_name} M1 代码任务清单\n\n## 核心模块\n1. PlayerController\n2. WeaponSystem\n3. EnemySystem\n4. XPSystem\n5. UISystem\n",
        f"{game_name}_{milestone}_测试任务清单.md": f"# {game_name} M1 测试任务清单\n\n## 冒烟测试\n1. 游戏启动\n2. 玩家移动\n3. 自动攻击\n4. 敌人生成\n5. XP升级\n",
    }
    
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    for filename, content in docs.items():
        filepath = out_path / filename
        filepath.write_text(content, encoding="utf-8")
        log_step(f"生成: {filename}", "OK")
    
    return True

# ============== 进度展示 ==============
def show_progress(current_step: int, total_steps: int, message: str = ""):
    bar_length = 30
    filled = int(bar_length * current_step / total_steps)
    bar = "█" * filled + "░" * (bar_length - filled)
    percent = int(100 * current_step / total_steps)
    
    print(f"\n{'='*60}")
    print(f"  自动化流水线进度: [{bar}] {percent}%")
    print(f"{'='*60}")
    
    if message:
        print(f"  状态: {message}\n")
    
    for i, step in enumerate(STEPS, 1):
        status = "✓" if i < current_step else ("→" if i == current_step else "○")
        auto_tag = "[自动]" if step.get("auto") else "[人工]"
        line = f"  {status} {i}. {step['name']} {auto_tag}"
        if i == current_step:
            print(f"{Colors.CYAN}{line}{Colors.ENDC}")
        elif i < current_step:
            print(f"{Colors.GREEN}{line}{Colors.ENDC}")
        else:
            print(f"{Colors.DIM}{line}{Colors.ENDC}")

def show_dispatch_files(game_name: str, milestone: str, output_dir: str):
    """显示生成的dispatch文件"""
    print(f"\n{Colors.GREEN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.GREEN}📁 已生成的任务包:{Colors.ENDC}")
    print(f"{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
    
    files = [
        f"{game_name}_整体里程碑规划.md",
        f"{game_name}_{milestone}_美术任务清单.md",
        f"{game_name}_{milestone}_代码任务清单.md",
        f"{game_name}_{milestone}_测试任务清单.md",
    ]
    
    for f in files:
        filepath = Path(output_dir) / f
        if filepath.exists():
            print(f"  {Colors.GREEN}✓{Colors.ENDC} {f}")
        else:
            print(f"  {Colors.RED}✗{Colors.ENDC} {f} (未生成)")
    
    print(f"\n  路径: {output_dir}\n")

# ============== 人工操作指引 ==============
def show_manual_actions(game_name: str):
    """显示需要人工操作的内容"""
    print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
    print(f"{Colors.YELLOW}👤 需要你（总指挥）做的:{Colors.ENDC}")
    print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}\n")
    
    print(f"  1. 派发任务给队友:")
    print(f"     - 美术队友 → {game_name}_M1_美术任务清单.md")
    print(f"     - 测试队友 → {game_name}_M1_测试任务清单.md")
    print(f"\n  2. 等待美术资源完成后，集成到Unity项目")
    print(f"\n  3. 代码自动化完成后，拉取构建包测试")
    print(f"\n  4. 反馈问题或确认完成\n")

# ============== 主函数 ==============
def main():
    parser = argparse.ArgumentParser(description="游戏复刻自动化流水线")
    parser.add_argument("--game", required=True, help="游戏名称")
    parser.add_argument("--milestone", default="M1", help="里程碑 (默认M1)")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="输出目录")
    parser.add_argument("--skip-agent", action="store_true", help="跳过AI agent（使用模板生成）")
    parser.add_argument("--base-url", default=os.getenv("OPENAI_BASE_URL", ""), help="API地址")
    parser.add_argument("--api-key", default=os.getenv("OPENAI_API_KEY", ""), help="API密钥")
    
    args = parser.parse_args()
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}")
    print("="*60)
    print("  🎮 游戏复刻自动化流水线")
    print("="*60)
    print(f"  游戏: {args.game}")
    print(f"  里程碑: {args.milestone}")
    print(f"  输出: {args.output_dir}")
    print(f"{Colors.ENDC}\n")
    
    # Step 1-3: 自动化任务分解
    current_step = 1
    show_progress(current_step, len(STEPS), "游戏分析与任务分解")
    
    if args.skip_agent:
        generate_dispatch_docs_manually(args.game, args.milestone, args.output_dir)
    else:
        if args.base_url and args.api_key:
            success = run_dispatch_agent(args.game, args.milestone, args.base_url, args.api_key)
            if not success:
                log_step("Agent失败，使用模板生成", "WARN")
                generate_dispatch_docs_manually(args.game, args.milestone, args.output_dir)
        else:
            log_step("未配置API，跳过agent生成", "WARN")
            generate_dispatch_docs_manually(args.game, args.milestone, args.output_dir)
    
    current_step = 4
    show_progress(current_step, len(STEPS))
    
    # 显示结果
    show_dispatch_files(args.game, args.milestone, args.output_dir)
    
    # 人工操作
    log_user_action("派发美术和测试任务给队友")
    show_manual_actions(args.game)
    
    print(f"\n{Colors.CYAN}下一步:{Colors.ENDC}")
    print("  1. 把文档派发给队友")
    print("  2. 回复 '代码' 启动代码自动化")
    print("  3. 回复 '状态' 查看当前进度\n")

if __name__ == "__main__":
    main()
