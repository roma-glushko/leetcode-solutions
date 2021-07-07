from unittest import TestCase

from . import TreeNode
from .symmetric_tree import SymmetricTree


class SymmetricTreeTest(TestCase):

    def test_symmetric_tree(self):
        solution = SymmetricTree()

        self.assertTrue(
            solution.isSymmetric(TreeNode(1))
        )

        self.assertTrue(
            solution.isSymmetric(
                TreeNode(
                     1,
                     left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                     right=TreeNode(2, left=TreeNode(4), right=TreeNode(3))
                )
            )
        )

        self.assertTrue(
            solution.isSymmetric(
                TreeNode(
                    1,
                    left=TreeNode(2, right=TreeNode(3)),
                    right=TreeNode(2, left=TreeNode(3))
                )
            )
        )

    def test_asymmetric_tree(self):
        solution = SymmetricTree()

        self.assertFalse(
            solution.isSymmetric(
                TreeNode(
                    1,
                    left=TreeNode(2, right=TreeNode(3)),
                    right=TreeNode(2, right=TreeNode(3))
                )
            )
        )

        self.assertFalse(
            solution.isSymmetric(
                TreeNode(
                    1,
                    left=TreeNode(0, left=TreeNode(3), right=TreeNode(4)),
                    right=TreeNode(2, left=TreeNode(4), right=TreeNode(3))
                )
            )
        )
