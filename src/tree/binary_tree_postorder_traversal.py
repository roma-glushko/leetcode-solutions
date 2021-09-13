from typing import List

from . import TreeNode


class BinaryTreePostorderTraversal:
    """
    Problem Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
    Complexity: Easy

    Runtime: 24 ms
    Memory: 14.3 MB
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        if not root:
            return []

        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)

        return result
