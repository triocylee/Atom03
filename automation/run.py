"""
游戏复刻 - 一键启动脚本

用法:
    python run.py                    # 交互式
    python run.py init "游戏名"       # 快速初始化
    python run.py status             # 查看状态
    python run.py test               # 测试最新构建
"""

import sys
import os
from pathlib import Path

# 颜色
class C:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def logo():
    print(f"""
{ C.CYAN }╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🎮  游戏复刻自动化工具箱                                   ║
║                                                           ║
║   零代码接触 · Agent驱动 · 快速复刻                         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{ C.ENDC }
    """)

def menu():
    logo()
    print(f"""
  { C.GREEN }1.{ C.ENDC } 🚀 初始化新项目
  { C.GREEN }2.{ C.ENDC } 📊 查看状态
  { C.GREEN }3.{ C.ENDC } 📋 任务看板
  { C.GREEN }4.{ C.ENDC } 🔨 启动代码自动化
  { C.GREEN }5.{ C.ENDC } 📦 打开构建目录
  { C.GREEN }6.{ C.ENDC } 📚 打开文档目录
  { C.YELLOW }0.{ C.ENDC } ❌ 退出
    """)
    
    choice = input(f"  { C.CYAN }选择:{ C.ENDC } ").strip()
    return choice

def init_project():
    game_name = input(f"\n  { C.CYAN }游戏名称:{ C.ENDC } ").strip()
    if not game_name:
        print(f"  { C.RED }游戏名称不能为空{ C.ENDC }")
        return
    
    print(f"\n  { C.GREEN }▶ 启动自动化流水线...{ C.ENDC }\n")
    
    os.system(f'python D:\\GJ\\automation\\auto_pipeline.py --game "{game_name}" --milestone M1')
    
    print(f"""
  { C.GREEN }✓ 任务包已生成{ C.ENDC }
  
  下一步:
  1. 派发美术任务 → 美术队友
  2. 派发测试任务 → 测试队友
  3. 启动代码自动化 → 选择选项4
    """)

def show_status():
    os.system('python D:\\GJ\\automation\\code_automation.py status')

def show_board():
    os.system('python D:\\GJ\\automation\\code_automation.py board')

def start_coding():
    project_name = input(f"\n  { C.CYAN }项目名称:{ C.ENDC } ").strip()
    game_name = input(f"  { C.CYAN }游戏名称:{ C.ENDC } ").strip()
    
    if not project_name or not game_name:
        print(f"  { C.RED }名称不能为空{ C.ENDC }")
        return
    
    print(f"\n  { C.GREEN }▶ 启动代码自动化...{ C.ENDC }\n")
    
    os.system(f'python D:\\GJ\\automation\\code_automation.py start --project "{project_name}" --game "{game_name}"')

def open_builds():
    builds = Path(r"D:\GJ\game-projects")
    if builds.exists():
        os.system(f'explorer "{builds}"')
    else:
        print(f"  { C.RED }构建目录不存在{ C.ENDC }")

def open_docs():
    docs = Path(r"D:\GJ\docs\dispatch")
    if docs.exists():
        os.system(f'explorer "{docs}"')
    else:
        print(f"  { C.RED }文档目录不存在{ C.ENDC }")

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "init" and len(sys.argv) > 2:
            game = sys.argv[2]
            print(f"初始化: {game}")
            os.system(f'python D:\\GJ\\automation\\auto_pipeline.py --game "{game}" --milestone M1')
            return
        elif cmd == "status":
            show_status()
            return
        elif cmd == "board":
            show_board()
            return
    
    while True:
        choice = menu()
        
        if choice == "1":
            init_project()
        elif choice == "2":
            show_status()
        elif choice == "3":
            show_board()
        elif choice == "4":
            start_coding()
        elif choice == "5":
            open_builds()
        elif choice == "6":
            open_docs()
        elif choice == "0":
            print(f"\n{ C.CYAN }再见！{ C.ENDC }\n")
            break
        else:
            print(f"  { C.RED }无效选择{ C.ENDC }")
        
        input(f"\n  { C.DIM }按Enter继续...{ C.ENDC }")

if __name__ == "__main__":
    main()
