from .construct_string_from_binary_tree import ConstructStringFromBinaryTree
from .. import TreeNode


def test_multiple_level_tree():
    solution = ConstructStringFromBinaryTree()
    assert (
        solution.tree2str(
            TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
        )
        == "1(2(4))(3)"
    )
    assert (
        solution.tree2str(
            TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))
        )
        == "1(2()(4))(3)"
    )
