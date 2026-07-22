from .three_sum import ThreeSum


def test_base_input():
    solution = ThreeSum()
    assert sorted(solution.threeSum2([-1, 0, 1, 2, -1, -4])) == sorted(
        [(-1, -1, 2), (-1, 0, 1)]
    )


def test_empty_case():
    solution = ThreeSum()
    assert sorted(solution.threeSum([])) == sorted([])


def test_too_little_elements_case():
    solution = ThreeSum()
    assert sorted(solution.threeSum([0])) == sorted([])
    assert sorted(solution.threeSum([1, -1])) == sorted([])
