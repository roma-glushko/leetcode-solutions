from unittest import TestCase

from src.tree import TreeNode
from .path_sum import PathSum

class PathSumTest(TestCase):
    """
    Problem Link: https://leetcode.com/problems/path-sum/
    Complexity: Easy

    """
    def test_positive_input(self):
        solution = PathSum()

        self.assertTrue(
            solution.hasPathSum(
                TreeNode(
                    5,
                    left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
                    right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1)))
                ),
                22
            ),
        )

    def test_negative_input(self):
        solution = PathSum()

        self.assertFalse(
            solution.hasPathSum(
                TreeNode(
                    1,
                    left=TreeNode(2),
                    right=TreeNode(3)
                ),
                5,
            ),
        )

        self.assertFalse(
            solution.hasPathSum(
                TreeNode(
                    1,
                    left=TreeNode(2),
                ),
                0,
            ),
        )

    def test_negative_values_input(self):
        solution = PathSum()

        self.assertTrue(
            solution.hasPathSum(
                TreeNode(
                    -2,
                    right=TreeNode(-3)
                ),
                -5,
            ),
        )