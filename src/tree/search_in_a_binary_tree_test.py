from unittest import TestCase

from . import TreeNode
from .search_in_a_binary_tree import SearchInABinaryTree


class SearchInABinaryTreeTest(TestCase):

    def test_existing_inputs(self):
        solution = SearchInABinaryTree()

        subtree: TreeNode = TreeNode(2, left=TreeNode(1), right=TreeNode(3))

        self.assertEqual(
            subtree,
            solution.searchBST(
                TreeNode(
                    4,
                    left=subtree,
                    right=TreeNode(7),
                ),
                2
            )
        )

    def test_notfound_input(self):
        solution = SearchInABinaryTree()

        self.assertEqual(
            [],
            solution.searchBST(
                TreeNode(
                    4,
                    left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                    right=TreeNode(7),
                ),
                5
            )
        )