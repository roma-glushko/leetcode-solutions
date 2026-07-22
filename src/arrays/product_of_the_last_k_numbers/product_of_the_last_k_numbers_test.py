from .product_of_the_last_k_numbers import ProductOfTheLastKNumbers


def test_base_case():
    solution = ProductOfTheLastKNumbers()
    for num in [3, 0, 2, 5, 4]:
        solution.add(num)
    assert 20 == solution.getProduct(2)
    assert 40 == solution.getProduct(3)
    assert 0 == solution.getProduct(4)
    solution.add(8)
    assert 32 == solution.getProduct(2)
    assert 0 == solution.getProduct(10)


def test_one_numbers_case():
    solution = ProductOfTheLastKNumbers()
    for num in [2, 4, 1, 7, 4, 1, 4, 2]:
        solution.add(num)
    assert 8 == solution.getProduct(3)
    assert 224 == solution.getProduct(5)
    assert 224 == solution.getProduct(6)
    assert 1792 == solution.getProduct(8)
    solution.add(4)


def test_long_sequence_case():
    solution = ProductOfTheLastKNumbers()
    for num in [1] * 100000:
        solution.add(num)
    assert 1 == solution.getProduct(100000)
