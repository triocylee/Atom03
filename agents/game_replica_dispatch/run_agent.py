import argparse
import os
from pathlib import Path

from openai import OpenAI
from openai import PermissionDeniedError
from openai import NotFoundError


SYSTEM_PROMPT = """You are a game remake dispatch planning agent.

You must produce dispatch-ready markdown docs for game development teams.
Default scope is core experience version unless user explicitly asks for higher scope.

Required outputs:
1) Overall milestone roadmap file
2) Milestone-specific role files for:
- Art
- Code
- QA

Hard rules:
- Organize by milestones (M1-M4 by default), not random system list.
- Be concise, direct, and executable.
- Every role doc must include:
  - stage goal
  - must-complete items
  - detailed tasks
  - execution order
  - deliverable format
  - naming convention
  - deliver-to target
  - done criteria
  - dependencies
  - start-now vs wait states
- Explicitly show who blocks whom and handoff chain.
"""


def generate_doc(
    client: OpenAI,
    api_mode: str,
    model: str,
    game_name: str,
    milestone: str,
    doc_type: str,
) -> str:
    user_prompt = f"""Game: {game_name}
Milestone: {milestone}
Document type: {doc_type}

Produce only markdown content for this single document.
Do not wrap in code fences.
Use Chinese.
"""
    if api_mode == "chat":
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
        return (resp.choices[0].message.content or "").strip()

    resp = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    return resp.output_text.strip()


def save_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate game remake dispatch docs.")
    parser.add_argument("--game", required=False, help="Game name, e.g. Raft")
    parser.add_argument("--milestone", default="M1", help="Target milestone, e.g. M1")
    parser.add_argument(
        "--model",
        default=os.getenv("LLM_MODEL", "gpt-4.1"),
        help="Model name exposed by your endpoint",
    )
    parser.add_argument(
        "--api-mode",
        choices=["responses", "chat"],
        default=os.getenv("OPENAI_API_MODE", "responses"),
        help="Use 'responses' for /v1/responses or 'chat' for /v1/chat/completions relay",
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("OPENAI_BASE_URL", "").strip(),
        help="OpenAI-compatible endpoint base URL, e.g. https://your-proxy/v1",
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("OPENAI_API_KEY", "").strip(),
        help="API key for your endpoint (can also use OPENAI_API_KEY env var)",
    )
    parser.add_argument(
        "--out-dir",
        default=r"D:\GJ\docs\dispatch",
        help="Output directory for generated markdown docs",
    )
    parser.add_argument(
        "--paths-only",
        action="store_true",
        help="Print only saved file paths",
    )
    args = parser.parse_args()

    if not args.game:
        args.game = input("请输入游戏名: ").strip()
    if not args.game:
        raise RuntimeError("游戏名不能为空。请通过 --game 传入，或在提示时输入。")

    if not args.base_url:
        raise RuntimeError(
            "Missing base URL. Set --base-url or OPENAI_BASE_URL "
            "(example: https://your-relay-domain/v1)."
        )
    if not args.api_key:
        raise RuntimeError(
            "Missing API key. Set --api-key or OPENAI_API_KEY."
        )

    client = OpenAI(
        api_key=args.api_key,
        base_url=args.base_url,
    )

    out_dir = Path(args.out_dir)
    files = {
        "overall": out_dir / f"{args.game}_整体里程碑规划.md",
        "art": out_dir / f"{args.game}_{args.milestone}_美术任务清单.md",
        "code": out_dir / f"{args.game}_{args.milestone}_代码任务清单.md",
        "qa": out_dir / f"{args.game}_{args.milestone}_测试任务清单.md",
    }

    try:
        generated = {
            "overall": generate_doc(
                client,
                args.api_mode,
                args.model,
                args.game,
                args.milestone,
                "整体里程碑规划",
            ),
            "art": generate_doc(
                client, args.api_mode, args.model, args.game, args.milestone, "美术任务清单"
            ),
            "code": generate_doc(
                client, args.api_mode, args.model, args.game, args.milestone, "代码任务清单"
            ),
            "qa": generate_doc(
                client, args.api_mode, args.model, args.game, args.milestone, "测试任务清单"
            ),
        }
    except PermissionDeniedError as exc:
        raise RuntimeError(
            "模型无权限或 Key 无权限。请更换 --model 或更换 API key。\n"
            "建议先运行 diagnose_relay.py 查可用 endpoint/model 组合。"
        ) from exc
    except NotFoundError as exc:
        raise RuntimeError(
            "接口路径或模型不存在。请检查 --base-url 是否包含正确的 /v1 路径，"
            "并确认 --api-mode 与网关兼容。"
        ) from exc

    for key, path in files.items():
        save_text(path, generated[key])

    if args.paths_only:
        for path in files.values():
            print(path)
        return

    print("Saved files:")
    for path in files.values():
        print(f"- {path}")


if __name__ == "__main__":
    main()
