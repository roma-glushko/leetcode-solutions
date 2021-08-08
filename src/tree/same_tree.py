from . import TreeNode


class SameTree:
    """
    Problem Link: https://leetcode.com/problems/same-tree/
    Complexity: Easy

    Runtime: 28ms
    Memory: 14.4MB
    """

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)