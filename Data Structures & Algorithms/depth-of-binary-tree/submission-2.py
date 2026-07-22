# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Level Order Traversal - BFS
        # Count how many levels we traversed
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        depth = 0

        while q:
            # for each node, unpack the entire level and count it
            for i in range(len(q)):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            depth +=1

        return depth