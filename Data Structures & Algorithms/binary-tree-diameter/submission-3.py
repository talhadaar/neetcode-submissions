# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS PostOrder
        stack = [root] if root else []
        cache = {None: (0,0)}

        while stack:
            curr = stack[-1]

            if curr.left and curr.left not in cache:
                stack.append(curr.left)
            elif curr.right and curr.right not in cache:
                stack.append(curr.right)
            else:
                curr = stack.pop()

                lh,ld = cache[curr.left]
                rh,rd = cache[curr.right]

                currDiameter = lh+rh
                cache[curr] = (1+max(lh,rh), max(currDiameter, rd,ld))

        return cache[root][1]