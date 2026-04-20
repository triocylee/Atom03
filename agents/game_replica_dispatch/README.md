# Game Replica Dispatch Agent

This agent generates dispatch-ready markdown docs for game remake planning:
1. Overall milestone roadmap
2. Art task list for one milestone
3. Code task list for one milestone
4. QA task list for one milestone

## 1) Setup

```powershell
cd D:\GJ\agents\game_replica_dispatch
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create environment variable:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_BASE_URL="https://your-relay-domain/v1"
$env:LLM_MODEL="gpt-4.1"
$env:OPENAI_API_MODE="responses"
```

## 2) Run

Generate default M1 docs (explicit game name):

```powershell
python .\run_agent.py --game Raft --milestone M1 --paths-only
```

Generate M2 docs:

```powershell
python .\run_agent.py --game Thronefall --milestone M2 --paths-only
```

Run with explicit relay params:

```powershell
python .\run_agent.py `
  --game Raft `
  --milestone M1 `
  --base-url "https://your-relay-domain/v1" `
  --api-key "your_relay_key" `
  --model "gpt-4.1" `
  --api-mode "responses" `
  --paths-only
```

If your relay only supports `/v1/chat/completions`, switch mode:

```powershell
python .\run_agent.py --game Raft --milestone M1 --api-mode chat --paths-only
```

Interactive mode (input any game name at runtime):

```powershell
python .\run_agent.py --milestone M1 --paths-only
```

## 3) Output Paths

Default output directory:

`D:\GJ\docs\dispatch`

Generated filenames:
1. `{game}_整体里程碑规划.md`
2. `{game}_{milestone}_美术任务清单.md`
3. `{game}_{milestone}_代码任务清单.md`
4. `{game}_{milestone}_测试任务清单.md`

## 4) Notes

1. Default planning scope is core experience version.
2. The script always writes files; `--paths-only` only affects console output.
3. Use UTF-8 editors to read Chinese markdown filenames and content.
4. Your relay must be OpenAI-compatible for this script shape.
5. Prefer `responses` mode when available. Use `chat` mode for legacy relays.
