from .find_all_duplicates_in_an_array import FindAllDuplicatedInAnArray


def test_base_input():
    solution = FindAllDuplicatedInAnArray()
    assert sorted(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == sorted([2, 3])
    assert sorted(solution.findDuplicates([1, 1, 2])) == sorted([1])


def test_no_duplicates_input():
    solution = FindAllDuplicatedInAnArray()
    assert sorted(solution.findDuplicates([1])) == sorted([])
