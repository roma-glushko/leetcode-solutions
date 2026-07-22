from .. import TreeNode
from .symmetric_tree import SymmetricTree


def test_symmetric_tree():
    solution = SymmetricTree()
    assert solution.isSymmetric(TreeNode(1))
    assert solution.isSymmetric(
        TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
            right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
        )
    )
    assert solution.isSymmetric(
        TreeNode(
            1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, left=TreeNode(3))
        )
    )


def test_asymmetric_tree():
    solution = SymmetricTree()
    assert not solution.isSymmetric(
        TreeNode(
            1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, right=TreeNode(3))
        )
    )
    assert not solution.isSymmetric(
        TreeNode(
            1,
            left=TreeNode(0, left=TreeNode(3), right=TreeNode(4)),
            right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
        )
    )
