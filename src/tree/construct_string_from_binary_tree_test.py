from unittest import TestCase

from src.tree import TreeNode
from construct_string_from_binary_tree import ConstructStringFromBinaryTree


class ConstructStringFromBinaryTreeTest(TestCase):
    def test_multiple_level_tree(self):
        solution = ConstructStringFromBinaryTree()

        self.assertTrue(
            '1(2(4))(3)',
            solution.tree2str(
                TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
            )
        )

        self.assertTrue(
            '1(2()(4))(3)',
            solution.tree2str(
                TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))
            )
        )
