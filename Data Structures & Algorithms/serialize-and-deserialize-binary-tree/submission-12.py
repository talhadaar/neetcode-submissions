# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Traverse and add to a list then join to make a str
        # Level Order Traversal

        res = []
        if not root:
            return 'N'

    
        q = deque()
        q.append(root)

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
        split = data.split(',')
        if split[0]=='N':
            return None

        root = TreeNode(int(split[0]))

        q = deque()
        q.append(root)

        i = 1
        while q:
            curr = q.popleft()
            if split[i]!='N':
                curr.left = TreeNode(int(split[i]))
                q.append(curr.left)
            i+=1
            if split[i]!='N':
                curr.right = TreeNode(int(split[i]))
                q.append(curr.right)
            i+=1

        return root