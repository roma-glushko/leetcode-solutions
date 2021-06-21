from unittest import TestCase

from . import TreeNode
from .binary_tree_preorder_traversal import BinaryTreePreorderTraversal


class BinaryTreePreorderTraversalTest(TestCase):

    def test_default_inputs(self):
        solution = BinaryTreePreorderTraversal()

        self.assertTrue(
            [1, 2, 3],
            solution.preorderTraversal(
                TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
            )
        )

    def test_empty_inputs(self):
        solution = BinaryTreePreorderTraversal()

        self.assertTrue([1], solution.preorderTraversal(TreeNode(1)))

    def test_stumb_inputs(self):
        solution = BinaryTreePreorderTraversal()

        self.assertTrue(
            [1, 2],
            solution.preorderTraversal(TreeNode(1, left=TreeNode(2)))
        )

        self.assertTrue(
            [1, 2],
            solution.preorderTraversal(TreeNode(1, right=TreeNode(2)))
        )