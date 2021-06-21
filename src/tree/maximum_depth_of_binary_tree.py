from . import TreeNode


class MaximumDepthOfBinaryTree:
    """
    Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Complexity: Easy
    """

    def get_max_depth(self, node: TreeNode, depth_level: int) -> int:
        current_depth_level: int = depth_level + 1

        left_max_depth: int = self.get_max_depth(node.left, current_depth_level) if node.left else 0
        right_max_depth: int = self.get_max_depth(node.right, current_depth_level) if node.right else 0

        return max(current_depth_level, left_max_depth, right_max_depth)

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.get_max_depth(root, 0)