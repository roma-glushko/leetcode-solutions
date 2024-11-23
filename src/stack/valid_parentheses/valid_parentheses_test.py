from unittest import TestCase

from .valid_parentheses import ValidParentheses


class ValidParenthesesTest(TestCase):
    def test_valid(self):
        solution = ValidParentheses()

        self.assertTrue(solution.isValid("()"))
        self.assertTrue(solution.isValid("()[]{}"))
        self.assertTrue(solution.isValid("{[]}"))

    def test_invalid(self):
        solution = ValidParentheses()

        self.assertFalse(solution.isValid("]"))
        self.assertFalse(solution.isValid("(]"))
        self.assertFalse(solution.isValid("([)]"))
