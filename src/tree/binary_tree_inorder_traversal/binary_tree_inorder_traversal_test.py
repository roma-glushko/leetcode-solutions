from .. import TreeNode
from .binary_tree_inorder_traversal import BinaryTreeInorderTraversal


def test_default_inputs():
    solution = BinaryTreeInorderTraversal()
    assert solution.inorderTraversal(
        TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    ) == [1, 3, 2]


def test_empty_inputs():
    solution = BinaryTreeInorderTraversal()
    assert solution.inorderTraversal(TreeNode(1)) == [1]


def test_stumb_inputs():
    solution = BinaryTreeInorderTraversal()
    assert solution.inorderTraversal(TreeNode(1, left=TreeNode(2))) == [2, 1]
    assert solution.inorderTraversal(TreeNode(1, right=TreeNode(2))) == [1, 2]
