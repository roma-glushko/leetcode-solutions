import re
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from typing import TypedDict
import yaml


class Problem(TypedDict):
    id: str
    topic: str
    name: str
    link: str
    complexity: str
    solution_files: list[Path] | None


def get_solutions(problem_dir: Path) -> list[Path]:
    solution_patterns: list[str] = [
        "*.py",
        "*.sql",
        "*.go",
    ]

    solution_files: list[Path] = []

    for solution_pattern in solution_patterns:
        for file_path in problem_dir.glob(solution_pattern):
            if "test" in file_path.name:
                # ignore tests
                continue

            if "__init__" in file_path.name:
                # ignore module files
                continue

            solution_files.append(file_path)

    return solution_files


def get_problems(root_dir: Path) -> list[Problem]:
    problems: list[Problem] = []

    for problem_file_path in root_dir.glob("*/*/problem.yaml"):
        with open(problem_file_path, "r") as problem_file:
            problem_data = yaml.safe_load(problem_file)

            problem_id = problem_data["id"]
            problem_topic = problem_data["topic"]
            problem_name = problem_data["name"]
            problem_link = problem_data["link"]
            problem_complexity = problem_data["complexity"]

            problem_solutions = get_solutions(problem_file_path.parent)

            if not problem_solutions:
                print(f"warn: {problem_id} is ignored because it has no solutions yet")

            problems.append(
                Problem(
                    id=problem_id,
                    topic=problem_topic,
                    name=problem_name,
                    link=problem_link,
                    complexity=problem_complexity,
                    solution_files=problem_solutions,
                )
            )

    return problems


def get_solution_link_on_github(solution_path: str) -> str:
    github_root_url: str = (
        "https://github.com/roma-glushko/leetcode-solutions/tree/master/src"
    )
    local_path_pattern: str = r"((.|\.|\/)*src)"

    github_solution_url: str = re.sub(
        local_path_pattern, github_root_url, str(solution_path), 0, re.MULTILINE
    )

    if not github_solution_url:
        raise RuntimeError(
            "Cannot generate Github solution link for {} solution".format(solution_path)
        )

    return github_solution_url


def get_title_from_filename(solution_path: str) -> str:
    solution_filename: str = str(Path(solution_path).name)

    return (
        solution_filename.replace(".py", "")
        .replace(".sql", "")
        .replace("_", " ")
        .title()
        .replace(" Ii", " II")
        .replace("Dfs", "DFS")
        .replace("Bfs", "BFS")
        .replace("Sql", "SQL")
        .replace("Lru", "LRU")
    )


def generate_section_markdown(problems: list[Problem]) -> str:
    total_problems = len(problems)

    markdown: str = "## Problem List \n\n"
    markdown += f"In total, there are {total_problems} problems solved. Find all of them below.\n"

    problems_by_topic = defaultdict(list)
    for problem in problems:
        problems_by_topic[problem["topic"]].append(problem)

    # sort keys alphabetically and problems by complexity
    complexity_order = {"easy": 1, "medium": 2, "hard": 3}
    problems_by_topic = dict(sorted(problems_by_topic.items()))

    # Sort problems by complexity within each topic
    for topic, topic_problems in problems_by_topic.items():
        problems_by_topic[topic] = sorted(
            topic_problems,
            key=lambda p: complexity_order.get(p["complexity"].lower(), float("inf")),
        )

    ext_lang = {
        ".py": "Python",
        ".sql": "SQL",
        ".go": "Go",
    }

    for topic, topic_problems in problems_by_topic.items():
        markdown += f"\n ### {get_title_from_filename(topic)} \n\n"

        for problem in topic_problems:
            solutions_md = [
                f"[{ext_lang[solution_path.suffix]}]({get_solution_link_on_github(solution_path)})"
                for solution_path in problem["solution_files"]
            ]

            problem_name = problem["name"]
            problem_link = problem["link"]
            problem_complexity = problem["complexity"]

            markdown += f"- ({problem_complexity}) [{problem_name}]({problem_link}) ({' | '.join(solutions_md)}) \n"

    markdown += "\n## Credits \n\n"
    markdown += (
        "Challenges were solved with ❤️ by [Roman Glushko](https://www.romaglushko.com/)"
    )

    return markdown


def update_readme_file(readme_path: Path, new_section_content: str) -> None:
    section_pattern: str = r"(?P<list_section>## Problem List (.|\s|)*)"

    with open(readme_path, "r") as readme_file:
        readme_content: str = readme_file.read()

    new_readme_content: str = re.sub(
        section_pattern, new_section_content, readme_content, 0, re.MULTILINE
    )

    if not new_readme_content:
        raise RuntimeError("Cannot update {} content".format(readme_path))

    with open(readme_path, "w") as readme_file:
        readme_file.write(new_readme_content)


def get_arg_parser() -> ArgumentParser:
    arg_parser = ArgumentParser(description="Problem List Generator")

    arg_parser.add_argument("--solution_dir", type=str, required=True)
    arg_parser.add_argument("--readme_path", type=str, required=True)

    return arg_parser


if __name__ == "__main__":
    args = get_arg_parser().parse_args()

    root_dir: Path = Path(args.solution_dir).absolute()
    readme_path: Path = Path(args.readme_path).absolute()

    print("Collecting information about problems..")
    problems = get_problems(root_dir)
    print(f"Found {len(problems)} problems")

    print("Generating a new list section..")
    markdown: str = generate_section_markdown(problems)

    print("Updating readme file..")
    update_readme_file(readme_path, markdown)
