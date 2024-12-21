from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_middle(
            left: Optional[ListNode], right: Optional[ListNode]
        ) -> Optional[ListNode]:
            slow = left
            fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convert_to_bst(
            left: Optional[ListNode], right: Optional[ListNode]
        ) -> Optional[TreeNode]:
            if left == right:
                return None

            mid = find_middle(left, right)
            node = TreeNode(mid.val)

            node.left = convert_to_bst(left, mid)
            node.right = convert_to_bst(mid.next, right)

            return node

        return convert_to_bst(head, None)

    def tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], current_path: List[int], current_sum: int):
            if not node:
                return

            current_path.append(node.val)
            current_sum += node.val

            if not node.left and not node.right and current_sum == targetSum:
                paths.append(list(current_path))

            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            current_path.pop()

        paths = []
        dfs(root, [], 0)
        return paths
