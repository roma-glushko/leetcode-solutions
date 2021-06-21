from typing import List

from . import TreeNode


class BinaryTreePreorderTraversal:
    """
    Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
    Complexity: Easy
    Runtime: 28ms
    Memory: 14.2MB
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = [root.val]

        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)

        return result