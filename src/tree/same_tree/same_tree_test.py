from .. import TreeNode
from .same_tree import SameTree


def test_same_trees():
    solution = SameTree()
    assert solution.isSameTree(
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
    )


def test_different_trees():
    solution = SameTree()
    assert not solution.isSameTree(
        TreeNode(1, left=TreeNode(2)), TreeNode(1, right=TreeNode(2))
    )
    assert not solution.isSameTree(
        TreeNode(1, left=TreeNode(2), right=TreeNode(1)),
        TreeNode(1, left=TreeNode(1), right=TreeNode(2)),
    )
