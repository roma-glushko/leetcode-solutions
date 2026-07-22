from .sort_colors import SortColors


def test_default_input():
    solution = SortColors()
    colors: list[int] = [2, 0, 2, 1, 1, 0]
    solution.sortColors(colors)
    assert [0, 0, 1, 1, 2, 2] == colors
    colors = [2, 0, 1]
    solution.sortColors(colors)
    assert [0, 1, 2] == colors
    colors = [0]
    solution.sortColors(colors)
    assert [0] == colors
    colors = [1]
    solution.sortColors(colors)
    assert [1] == colors
