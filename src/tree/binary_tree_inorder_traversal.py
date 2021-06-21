from typing import List

from . import TreeNode


class BinaryTreeInorderTraversal:
    """
    Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
    Complexity: Easy

    Runtime: 32ms
    Memory: 14MB
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        if not root:
            return []

        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result