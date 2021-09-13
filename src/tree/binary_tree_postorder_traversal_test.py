from unittest import TestCase

from . import TreeNode
from .binary_tree_inorder_traversal import BinaryTreeInorderTraversal


class BinaryTreePostorderTraversalTest(TestCase):
    def test_default_inputs(self):
        solution = BinaryTreeInorderTraversal()

        self.assertTrue(
            [3, 2, 1],
            solution.inorderTraversal(
                TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
            ),
        )

    def test_empty_inputs(self):
        solution = BinaryTreeInorderTraversal()

        self.assertTrue([1], solution.inorderTraversal(TreeNode(1)))

    def test_stumb_inputs(self):
        solution = BinaryTreeInorderTraversal()

        self.assertTrue(
            [2, 1], solution.inorderTraversal(TreeNode(1, left=TreeNode(2)))
        )

        self.assertTrue(
            [2, 1], solution.inorderTraversal(TreeNode(1, right=TreeNode(2)))
        )
