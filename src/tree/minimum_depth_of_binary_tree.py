import math
import sys

from src.tree import TreeNode


class MinimumDepthOfBinaryTree:
    """
    Problem Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
    Complexity: Easy
    """

    def get_min_depth(self, node: TreeNode, current_depth: int) -> int:
        if not node.left and not node.right:
            # found a leaf
            return current_depth + 1

        return min(
            self.get_min_depth(node.left, current_depth + 1) if node.left else math.inf,
            self.get_min_depth(node.right, current_depth + 1) if node.right else math.inf,
        )

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.get_min_depth(root, 0)