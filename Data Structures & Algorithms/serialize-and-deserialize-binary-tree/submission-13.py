# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Level Order Traversal

        res = []
        q = deque([root])

        while q:
            curr = q.popleft()
            if curr:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                res.append('N')
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')

        if data[0] == 'N':
            return None

        root = TreeNode(int(data[0]))
        q = deque([root])
        i = 1

        while q:
            curr = q.popleft()
            if data[i]!='N':
                t = TreeNode(int(data[i]))
                curr.left = t
                q.append(t)
            i+=1
            if data[i]!='N':
                t = TreeNode(int(data[i]))
                curr.right = t
                q.append(t)
            i+=1
        return root