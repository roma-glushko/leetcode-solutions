from .. import TreeNode
from .maximum_depth_of_binary_tree import MaximumDepthOfBinaryTree


def test_multiple_level_tree():
    solution = MaximumDepthOfBinaryTree()
    assert (
        solution.maxDepth(
            TreeNode(
                3,
                left=TreeNode(9),
                right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
            )
        )
        == 3
    )


def test_single_level_tree():
    solution = MaximumDepthOfBinaryTree()
    assert solution.maxDepth(TreeNode(1, right=TreeNode(2))) == 2


def test_stumb_inputs():
    solution = MaximumDepthOfBinaryTree()
    assert solution.maxDepth(TreeNode(0)) == 1
