# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        q = [root]
        while q:
            qLen = len(q)
            lvl = []
            for i in range(qLen):
                curr = q.pop(0)
                if curr:
                    lvl.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if lvl:
                res.append(lvl)
        return res
