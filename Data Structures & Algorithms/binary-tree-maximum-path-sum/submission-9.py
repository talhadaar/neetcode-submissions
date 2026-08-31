# Definition for a binary tree node.
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Max Path Sum
        # InOrder traversal: Keep a running maxSum and a localSum. Reset Local sum when a <0 val is seen. Kdane's algo?
        # A Path is Parent + adjacent Children only? YES
        # So a path sum is Parent.val + max(leftPathSum, rightPathSum)

        res = [root.val]
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]