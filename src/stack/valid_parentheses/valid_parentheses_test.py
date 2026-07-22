from .valid_parentheses import ValidParentheses


def test_valid():
    solution = ValidParentheses()
    assert solution.isValid("()")
    assert solution.isValid("()[]{}")
    assert solution.isValid("{[]}")


def test_invalid():
    solution = ValidParentheses()
    assert not solution.isValid("]")
    assert not solution.isValid("(]")
    assert not solution.isValid("([)]")
