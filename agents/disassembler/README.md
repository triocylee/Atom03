# Disassembler Agent

`disassembler` agent receives a game name and decomposes it into dispatch-ready remake documents.

It is constrained to the contract of `game-replica-dispatch` skill:
1. Milestone-first planning (`M1` to `M4`)
2. Role split fixed to `Art / Code / QA`
3. Default scope is core experience version

## Setup

```powershell
cd D:\GJ\agents\disassembler
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Environment variables:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_BASE_URL="https://your-relay-domain/v1"
$env:LLM_MODEL="gpt-4.1"
$env:OPENAI_API_MODE="responses"
```

## Run

```powershell
python .\run_agent.py --game Raft --milestone M1 --paths-only
```

Interactive game input:

```powershell
python .\run_agent.py --milestone M1 --paths-only
```

## Output

Default output folder:

`D:\GJ\docs\dispatch`

Generated files:
1. `{game}_整体里程碑规划.md`
2. `{game}_{milestone}_美术任务清单.md`
3. `{game}_{milestone}_代码任务清单.md`
4. `{game}_{milestone}_测试任务清单.md`
