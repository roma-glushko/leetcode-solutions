from .reverse_string import ReverseString


def test_default_input():
    solution = ReverseString()
    result_array = ["h", "e", "l", "l", "o"]
    solution.reverse_string(result_array)
    assert result_array == ["o", "l", "l", "e", "h"]
