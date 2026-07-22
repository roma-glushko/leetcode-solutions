from .number_of_islands import NumberOfIslands


def test_big_island():
    solution = NumberOfIslands()
    num_of_islands = solution.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
    assert num_of_islands == 1


def test_three_islands():
    solution = NumberOfIslands()
    area = solution.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
    assert area == 3


def test_no_islands():
    solution = NumberOfIslands()
    area = solution.numIslands(
        [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
    assert area == 0


def test_one_huge_island():
    solution = NumberOfIslands()
    area = solution.numIslands(
        [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
        ]
    )
    assert area == 1
