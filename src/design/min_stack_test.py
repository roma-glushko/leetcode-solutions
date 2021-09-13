from unittest import TestCase

from .min_stack import MinStack


class MinStackTest(TestCase):
    def test_default_input(self):
        min_stack = MinStack()

        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)

        self.assertEqual(min_stack.getMin(), -3)

        min_stack.pop()

        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.getMin(), -2)
