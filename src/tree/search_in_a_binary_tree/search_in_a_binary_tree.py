from src.tree import TreeNode


class SearchInABinaryTree:
    """
    Problem Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
    Complexity: Easy
    """

    def searchBST(self, root: TreeNode, val: int) -> TreeNode | None:
        if root and root.val == val:
            return root

        if root.val < val:
            # wanna find a bigger value
            return self.searchBST(root.right, val)

        if root.val > val:
            # wanna find a smaller value
            return self.searchBST(root.left, val)

        return None
