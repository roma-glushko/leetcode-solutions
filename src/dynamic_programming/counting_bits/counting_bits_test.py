from .counting_bits import CountingBits


def test_default_inputs():
    solution = CountingBits()
    bit_array = solution.countBits(2)
    assert bit_array == [0, 1, 1]
    bit_array = solution.countBits(3)
    assert bit_array == [0, 1, 1, 2]
    bit_array = solution.countBits(4)
    assert bit_array == [0, 1, 1, 2, 1]
    bit_array = solution.countBits(5)
    assert bit_array == [0, 1, 1, 2, 1, 2]


def test_base_cases():
    solution = CountingBits()
    bit_array = solution.countBits(0)
    assert bit_array == [0]
    bit_array = solution.countBits(1)
    assert bit_array == [0, 1]
