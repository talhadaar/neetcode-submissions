# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        cache = defaultdict(int)
        cache[None] = 0
        best = root.val
        stack = [root]

        while stack:
            curr = stack[-1]

            if curr.left and curr.left not in cache:
                stack.append(curr.left)
            elif curr.right and curr.right not in cache:
                stack.append(curr.right)
            else:
                curr = stack.pop()

                ls = cache[curr.left]
                rs = cache[curr.right]

                ls = max(0, ls)
                rs = max(0, rs)

                best = max(best, curr.val + ls + rs)

                cache[curr] = curr.val + max(ls,rs)
        return best