from unittest import TestCase

from . import TreeNode
from .same_tree import SameTree


class SameTreeTest(TestCase):
    def test_same_trees(self):
        solution = SameTree()

        self.assertTrue(
            solution.isSameTree(
                TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
                TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
            )
        )

    def test_different_trees(self):
        solution = SameTree()

        self.assertFalse(
            solution.isSameTree(
                TreeNode(1, left=TreeNode(2)),
                TreeNode(1, right=TreeNode(2)),
            )
        )

        self.assertFalse(
            solution.isSameTree(
                TreeNode(1, left=TreeNode(2), right=TreeNode(1)),
                TreeNode(1, left=TreeNode(1), right=TreeNode(2)),
            )
        )
