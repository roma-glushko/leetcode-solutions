from src.tree import TreeNode


class ConstructStringFromBinaryTree:
    """
    Problem Link: https://leetcode.com/problems/construct-string-from-binary-tree/
    Complexity: Easy

    Runtime: 56ms
    Memory: 16.3MB
    """

    empty_tree_str: str = "()"

    def is_empty(self, subtree_str: str):
        return subtree_str == self.empty_tree_str

    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""

        result = f"{root.val}"

        left_subtree_str: str = f"({self.tree2str(root.left)})"
        right_subtree_str: str = f"({self.tree2str(root.right)})"

        if self.is_empty(left_subtree_str) and self.is_empty(right_subtree_str):
            return result

        if not self.is_empty(left_subtree_str) and self.is_empty(right_subtree_str):
            return f"{result}{left_subtree_str}"

        return f"{result}{left_subtree_str}{right_subtree_str}"
