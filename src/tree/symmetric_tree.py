from src.tree import TreeNode


class SymmetricTree:
    """
    Problem Link: https://leetcode.com/problems/symmetric-tree/
    Complexity: Easy

    Runtime: 32ms
    Memory: 14.4MB
    """
    def is_two_nodes_symmetric(self, left_node: TreeNode, right_node: TreeNode) -> bool:
        if not left_node and right_node:
            return False

        if left_node and not right_node:
            return False

        if not left_node and not right_node:
            return True

        if left_node.val != right_node.val:
            return False

        return self.is_two_nodes_symmetric(left_node.right, right_node.left) \
               and self.is_two_nodes_symmetric(left_node.left, right_node.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_two_nodes_symmetric(root.left, root.right)

