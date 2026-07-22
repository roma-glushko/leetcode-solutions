from .. import TreeNode
from .binary_tree_preorder_traversal import BinaryTreePreorderTraversal


def test_default_inputs():
    solution = BinaryTreePreorderTraversal()
    assert solution.preorderTraversal(
        TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    ) == [1, 2, 3]


def test_empty_inputs():
    solution = BinaryTreePreorderTraversal()
    assert solution.preorderTraversal(TreeNode(1)) == [1]


def test_stumb_inputs():
    solution = BinaryTreePreorderTraversal()
    assert solution.preorderTraversal(TreeNode(1, left=TreeNode(2))) == [1, 2]
    assert solution.preorderTraversal(TreeNode(1, right=TreeNode(2))) == [1, 2]
