from .. import TreeNode
from .binary_tree_postorder_traversal import BinaryTreePostorderTraversal


def test_default_inputs():
    solution = BinaryTreePostorderTraversal()
    assert solution.postorderTraversal(
        TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    ) == [3, 2, 1]


def test_empty_inputs():
    solution = BinaryTreePostorderTraversal()
    assert solution.postorderTraversal(TreeNode(1)) == [1]


def test_stumb_inputs():
    solution = BinaryTreePostorderTraversal()
    assert solution.postorderTraversal(TreeNode(1, left=TreeNode(2))) == [2, 1]
    assert solution.postorderTraversal(TreeNode(1, right=TreeNode(2))) == [2, 1]
