from .. import TreeNode
from .search_in_a_binary_tree import SearchInABinaryTree


def test_existing_inputs():
    solution = SearchInABinaryTree()
    subtree: TreeNode = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    assert subtree == solution.searchBST(
        TreeNode(4, left=subtree, right=TreeNode(7)), 2
    )


def test_notfound_input():
    solution = SearchInABinaryTree()
    assert [] == solution.searchBST(
        TreeNode(
            4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7)
        ),
        5,
    )
