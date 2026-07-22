from .reverse_integer import ReverseInteger


def test_default_input():
    solution = ReverseInteger()
    reversed_number = solution.reverse(123)
    assert reversed_number == 321
