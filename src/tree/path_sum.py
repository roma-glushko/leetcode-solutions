from src.tree import TreeNode


class PathSum:
    """
    Problem Link: https://leetcode.com/problems/path-sum/
    Complexity: Easy

    Runtime: 36ms
    Memory: 16MB
    """
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.right and not root.left:
            if targetSum == 0:
                # found a path that equal to targetSum
                return True

            # already leaf but targetSum is not diminished
            return False

        return self.hasPathSum(root.left, targetSum) or \
               self.hasPathSum(root.right, targetSum)