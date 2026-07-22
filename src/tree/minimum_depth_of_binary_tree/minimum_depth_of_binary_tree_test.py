from .. import TreeNode
from .minimum_depth_of_binary_tree import MinimumDepthOfBinaryTree


def test_multiple_level_tree():
    solution = MinimumDepthOfBinaryTree()
    assert (
        solution.minDepth(
            TreeNode(
                3,
                left=TreeNode(9),
                right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
            )
        )
        == 2
    )


def test_unbalanced_tree():
    solution = MinimumDepthOfBinaryTree()
    assert (
        solution.minDepth(
            TreeNode(
                2,
                right=TreeNode(
                    3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))
                ),
            )
        )
        == 5
    )
