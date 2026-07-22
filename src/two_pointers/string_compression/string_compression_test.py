from .string_compression import StringCompress


def test_three_chars():
    solution = StringCompress()
    string = ["a", "a", "b", "b", "c", "c", "c"]
    expected_result = ["a", "2", "b", "2", "c", "3"]
    expected_len: int = len(expected_result)
    length: int = solution.compress(string)
    assert expected_result == string[0:length]
    assert expected_len == length


def test_one_chars():
    solution = StringCompress()
    string = ["a"]
    expected_result = ["a"]
    length: int = solution.compress(string)
    assert string == expected_result
    assert length == len(expected_result)


def test_two_the_same_chars():
    solution = StringCompress()
    string = ["a", "a"]
    expected_result = ["a", "2"]
    length: int = solution.compress(string)
    assert expected_result == string
    assert len(expected_result) == length


def test_wb_chars():
    solution = StringCompress()
    string = [
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "B",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "B",
        "B",
        "B",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "B",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
    ]
    expected_result = [
        "W",
        "1",
        "2",
        "B",
        "W",
        "1",
        "2",
        "B",
        "3",
        "W",
        "2",
        "4",
        "B",
        "W",
        "1",
        "4",
    ]
    length: int = solution.compress(string)
    assert expected_result == string[0:length]
    assert len(expected_result) == length
