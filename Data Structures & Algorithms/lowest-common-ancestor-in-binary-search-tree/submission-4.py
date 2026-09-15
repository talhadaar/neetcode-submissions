# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        node = root

        while node:
            if max(p.val,q.val) < node.val:
                node = node.left
            elif min(p.val,q.val) > node.val:
                node = node.right
            else:
                return node