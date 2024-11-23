from unittest import TestCase

from . import TreeNode
from .minimum_depth_of_binary_tree import MinimumDepthOfBinaryTree


class MinimumDepthOfBinaryTreeTest(TestCase):
    def test_multiple_level_tree(self):
        solution = MinimumDepthOfBinaryTree()

        self.assertTrue(
            2,
            solution.minDepth(
                TreeNode(
                    3,
                    left=TreeNode(9),
                    right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
                )
            ),
        )

    def test_unbalanced_tree(self):
        solution = MinimumDepthOfBinaryTree()

        self.assertTrue(
            5,
            solution.minDepth(
                TreeNode(
                    2,
                    right=TreeNode(
                        3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))
                    ),
                )
            ),
        )
