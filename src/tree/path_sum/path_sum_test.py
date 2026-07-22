from .. import TreeNode
from .path_sum import PathSum


def test_positive_input():
    solution = PathSum()
    assert solution.hasPathSum(
        TreeNode(
            5,
            left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
            right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))),
        ),
        22,
    )


def test_negative_input():
    solution = PathSum()
    assert not solution.hasPathSum(TreeNode(1, left=TreeNode(2), right=TreeNode(3)), 5)
    assert not solution.hasPathSum(TreeNode(1, left=TreeNode(2)), 0)


def test_negative_values_input():
    solution = PathSum()
    assert solution.hasPathSum(TreeNode(-2, right=TreeNode(-3)), -5)
