from unittest import TestCase

from .jump_game_ii import JumpGameII


class JumpGameIITest(TestCase):

    def test_default_input(self):
        solution = JumpGameII()

        self.assertEqual(
            2,
            solution.jump([2, 3, 1, 1, 4])
        )

        self.assertEqual(
            2,
            solution.jump([2, 3, 0, 1, 4])
        )

        self.assertEqual(
            2,
            solution.jump([2, 3, 0, 1])
        )

        self.assertEqual(
            0,
            solution.jump([2])
        )

        self.assertEqual(
            3,
            solution.jump([1, 2, 1, 1, 1])
        )

        self.assertEqual(
            2,
            solution.jump([2, 5, 1, 1, 1])
        )

        self.assertEqual(
            1,
            solution.jump([100, 1, 1, 1, 1])
        )

        self.assertEqual(
            4,
            solution.jump([1, 1, 1, 1, 1])
        )