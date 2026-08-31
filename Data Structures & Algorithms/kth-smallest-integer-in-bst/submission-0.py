# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS(InOrder)
        stack, cur = [], root
        while stack or cur:
            while cur:              # dive left, remembering the path
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()       # Smallest value popped
            k -= 1                  # count smallest value
            if k == 0:              # return if reached k'th smallest
                return cur.val
            cur = cur.right         # Now traverse right subtree