import random
import subprocess
from argparse import ArgumentParser
from datetime import date, datetime
from pathlib import Path

import yaml


def get_problems(root_dir: Path) -> list[dict]:
    problems: list[dict] = []

    for problem_file_path in root_dir.glob("*/*/problem.yaml"):
        with open(problem_file_path, "r") as f:
            data = yaml.safe_load(f)

        problems.append(
            {
                "id": data["id"],
                "name": data["name"],
                "complexity": data["complexity"],
                "topic": data["topic"],
                "link": data["link"],
                "last_reviewed": data.get("last_reviewed"),
                "yaml_path": problem_file_path,
                "dir": problem_file_path.parent,
            }
        )

    return problems


def get_last_git_date(problem_dir: Path) -> date | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "--", str(problem_dir)],
            capture_output=True,
            text=True,
            check=True,
        )
        date_str = result.stdout.strip()
        if date_str:
            return datetime.fromisoformat(date_str).date()
    except subprocess.CalledProcessError:
        pass

    return None


def get_last_solved(problem: dict) -> date | None:
    if problem["last_reviewed"]:
        return date.fromisoformat(str(problem["last_reviewed"]))

    return get_last_git_date(problem["dir"])


def save_suggestion(gym_dir: Path, suggestions: list[dict]) -> None:
    gym_dir.mkdir(parents=True, exist_ok=True)
    suggestion_path = gym_dir / "suggestion.yaml"

    data = [
        {"id": s["id"], "name": s["name"], "yaml_path": str(s["yaml_path"])}
        for s in suggestions
    ]

    with open(suggestion_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False)


def load_suggestion(gym_dir: Path) -> list[dict]:
    suggestion_path = gym_dir / "suggestion.yaml"

    if not suggestion_path.exists():
        print("No recent suggestion found. Run 'suggest' first.")
        raise SystemExit(1)

    with open(suggestion_path, "r") as f:
        data = yaml.safe_load(f)

    return data or []


def update_problem_yaml(yaml_path: Path, reviewed_date: str) -> None:
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    data["last_reviewed"] = reviewed_date

    with open(yaml_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=True)


def cmd_suggest(args) -> None:
    root_dir = Path(args.solution_dir).absolute()
    gym_dir = Path(".gym")
    count = args.count

    problems = get_problems(root_dir)

    for problem in problems:
        problem["_last_solved"] = get_last_solved(problem)

    problems.sort(key=lambda p: p["_last_solved"] or date.min)

    pool_size = args.pool
    pool = problems[:pool_size]
    suggestions = random.sample(pool, min(count, len(pool)))
    today = date.today()

    print("\n🏋️ LeetCode Gym - Time to review:\n")
    print(
        f" {'#':>2}  {'Problem':<35} {'Complexity':<12} {'Topic':<20} {'Last Solved':<14} {'Days Ago':>8}"
    )
    print(f" {'─' * 2}  {'─' * 35} {'─' * 12} {'─' * 20} {'─' * 14} {'─' * 8}")

    for i, problem in enumerate(suggestions, 1):
        last = problem["_last_solved"]
        if last:
            last_str = last.isoformat()
            days_ago = str((today - last).days)
        else:
            last_str = "unknown"
            days_ago = "?"

        print(
            f" {i:>2}  {problem['name']:<35} {problem['complexity']:<12} "
            f"{problem['topic']:<20} {last_str:<14} {days_ago:>8}"
        )

    print()
    save_suggestion(gym_dir, suggestions)


def cmd_submit(args) -> None:
    gym_dir = Path(".gym")
    suggestions = load_suggestion(gym_dir)

    print("\nRecently suggested challenges:\n")
    for i, s in enumerate(suggestions, 1):
        print(f"  {i}. {s['name']}")

    print()
    raw = input(
        "Which challenges did you complete? (comma-separated numbers, e.g. 1,3): "
    )

    try:
        indices = [int(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError:
        print("Invalid input.")
        raise SystemExit(1)

    today_str = date.today().isoformat()

    print()
    for idx in indices:
        if idx < 1 or idx > len(suggestions):
            print(f"  Skipping invalid number: {idx}")
            continue

        problem = suggestions[idx - 1]
        yaml_path = Path(problem["yaml_path"])
        update_problem_yaml(yaml_path, today_str)
        print(f"  ✅ Recorded: {problem['name']} ({today_str})")

    print()


def get_arg_parser() -> ArgumentParser:
    parser = ArgumentParser(description="LeetCode Gym - Spaced review for challenges")
    subparsers = parser.add_subparsers(dest="command", required=True)

    suggest_parser = subparsers.add_parser(
        "suggest", help="Suggest challenges to review"
    )
    suggest_parser.add_argument("--solution_dir", type=str, required=True)
    suggest_parser.add_argument("--count", type=int, default=1)
    suggest_parser.add_argument(
        "--pool", type=int, default=20, help="Pick from the N oldest challenges"
    )

    submit_parser = subparsers.add_parser("submit", help="Record completed challenges")
    submit_parser.add_argument("--solution_dir", type=str, required=True)

    return parser


if __name__ == "__main__":
    args = get_arg_parser().parse_args()

    if args.command == "suggest":
        cmd_suggest(args)
    elif args.command == "submit":
        cmd_submit(args)
