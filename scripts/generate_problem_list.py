import glob
import os
import re
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from typing import List, Dict


def get_list_of_solution_files(root_dir: str) -> List[str]:
    solution_pattern: str = os.path.join(root_dir, '*', '*.py')

    solution_files: List[str] = []

    for file_path in glob.glob(solution_pattern):
        if 'test' in file_path:
            # ignore tests
            continue

        if '__init__' in file_path:
            # ignore module files
            continue

        solution_files.append(file_path)

    return solution_files


def get_title_from_filename(solution_path: str) -> str:
    solution_filename: str = str(Path(solution_path).name)

    return solution_filename \
        .replace('.py', '') \
        .replace('_', ' ') \
        .title() \
        .replace(' Ii', ' II') \
        .replace('Dfs', 'DFS') \
        .replace('Bfs', 'BFS') \
        .replace('Lru', 'LRU') \


def get_solution_link_on_github(solution_path: str) -> str:
    github_root_url: str = 'https://github.com/roma-glushko/leetcode-solutions/tree/master/src'
    local_path_pattern: str = r'((.|\.|\/)*src)'

    github_solution_url: str = re.sub(local_path_pattern, github_root_url, solution_path, 0, re.MULTILINE)

    if not github_solution_url:
        raise RuntimeError('Cannot generate Github solution link for {} solution'.format(solution_path))

    return github_solution_url


def parse_problem_info(solution_paths: List[str]) -> Dict[str, List[Dict]]:
    link_pattern: str = r'Problem Link:\s(?P<link>https:\/\/.*)$'
    complexity_pattern: str = r'Complexity:\s(?P<complexity>.*)$'

    solutions: Dict[str, List[Dict]] = defaultdict(list)

    for solution_path in solution_paths:
        with open(solution_path, 'r') as file:
            solution_content: str = file.read()

            solution_topic: str = str(Path(solution_path).parent.name)
            solution_title: str = get_title_from_filename(solution_path)

            solution_info: Dict = {
                'path': solution_path,
                'title': solution_title,
                'link': '',
                'complexity': '',
            }

            link_matches: re.Match = re.search(link_pattern, solution_content, re.MULTILINE)
            complexity_matches: re.Match = re.search(complexity_pattern, solution_content, re.MULTILINE)

            if link_matches:
                solution_info['link'] = link_matches.group('link')
            else:
                print('[warn] Solution {} doesn\'t have link specified'.format(solution_path))

            if complexity_matches:
                solution_info['complexity'] = complexity_matches.group('complexity')
            else:
                print('[warn] Solution {} doesn\'t have complexity specified'.format(solution_path))

            solutions[solution_topic].append(solution_info)

    return solutions


def generate_section_markdown(solutions: Dict[str, List[Dict]]) -> str:
    total_solutions: int = sum(
        list(map(
            lambda solution_list: len(solution_list),
            list(solutions.values()),
        ))
    )

    markdown: str = '## Problem List \n\n'
    markdown += 'In total, there are {} problems solved. Find all of them below.\n'.format(total_solutions)

    for topic in sorted(list(solutions.keys())):
        markdown += '\n ### {} \n\n'.format(get_title_from_filename(topic))

        topic_solutions = solutions[topic]
        # todo: sort by complexity

        for solution in topic_solutions:
            markdown += '- [{}]({}) ([Solution]({})) \n'.format(
                solution['title'],
                solution['link'],
                get_solution_link_on_github(solution['path'])
            )

    markdown += '\n## Credits \n\n'
    markdown += 'Challenged were solved with ❤️ by [Roman Glushko](https://www.romaglushko.com/)'

    return markdown


def update_readme_file(readme_path: str, new_section_content: str) -> None:
    section_pattern: str = r"(?P<list_section>## Problem List (.|\s|)*)"

    with open(readme_path, 'r') as readme_file:
        readme_content: str = readme_file.read()

    new_readme_content: str = re.sub(section_pattern, new_section_content, readme_content, 0, re.MULTILINE)

    if not new_readme_content:
        raise RuntimeError('Cannot update {} content'.format(readme_path))

    with open(readme_path, 'w') as readme_file:
        readme_file.write(new_readme_content)


def get_arg_parser() -> ArgumentParser:
    arg_parser = ArgumentParser(description='Problem List Generator')

    arg_parser.add_argument('--solution_dir', type=str, required=True)
    arg_parser.add_argument('--readme_path', type=str, required=True)

    return arg_parser


if __name__ == "__main__":
    args = get_arg_parser().parse_args()

    root_dir: str = args.solution_dir
    readme_path: str = args.readme_path

    print('Collecting information about solutions..')
    solution_files = get_list_of_solution_files(root_dir)
    solutions = parse_problem_info(solution_files)

    print('Generating a new list section..')
    markdown: str = generate_section_markdown(solutions)

    print('Updating readme file..')
    update_readme_file(readme_path, markdown)
