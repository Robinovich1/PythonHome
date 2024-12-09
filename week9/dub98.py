from typing import Optional

from week5.hash105 import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function to perform the recursion
        def helper(node, min_val, max_val):
            if not node:
                return True  # An empty tree is a valid BST

            # The current node's value must be within the valid range
            if not (min_val < node.val < max_val):
                return False

            # Recursively check left and right subtrees with updated range
            return helper(node.left, min_val, node.val) and helper(
                node.right, node.val, max_val
            )

        # Initial call with the entire range of possible integer values
        return helper(root, float("-inf"), float("inf"))
