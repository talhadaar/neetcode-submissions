# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Parent + LC + RC = path
        # val(Parent) + LC + RC = sum
  
        def dfs(root: Optional(TreeNode), maxPathSum):
            if not root:
                return 0
            
            lps = max(0, dfs(root.left, maxPathSum))
            rps = max(0, dfs(root.right, maxPathSum))
            pathSum = root.val + lps + rps

            maxPathSum[0] = max(maxPathSum[0], pathSum)
            return root.val + max(lps, rps)
        
        maxPathSum = [float('-inf')]
        dfs(root, maxPathSum)
        return maxPathSum[0]