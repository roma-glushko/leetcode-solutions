from unittest import TestCase

from . import TreeNode
from .maximum_depth_of_binary_tree import MaximumDepthOfBinaryTree


class MaximumDepthOfBinaryTreeTest(TestCase):

    def test_multiple_level_tree(self):
        solution = MaximumDepthOfBinaryTree()

        self.assertTrue(
            3,
            solution.maxDepth(
                TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
            )
        )

    def test_single_level_tree(self):
        solution = MaximumDepthOfBinaryTree()

        self.assertTrue(2, solution.maxDepth(TreeNode(1, right=TreeNode(2))))

    def test_stumb_inputs(self):
        solution = MaximumDepthOfBinaryTree()

        self.assertTrue(
            1,
            solution.maxDepth(TreeNode(0))
        )