from .jump_game_ii import JumpGameII


def test_default_input():
    solution = JumpGameII()
    assert 2 == solution.jump([2, 3, 1, 1, 4])
    assert 2 == solution.jump([2, 3, 0, 1, 4])
    assert 2 == solution.jump([2, 3, 0, 1])
    assert 0 == solution.jump([2])
    assert 3 == solution.jump([1, 2, 1, 1, 1])
    assert 2 == solution.jump([2, 5, 1, 1, 1])
    assert 1 == solution.jump([100, 1, 1, 1, 1])
    assert 4 == solution.jump([1, 1, 1, 1, 1])
