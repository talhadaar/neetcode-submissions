# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # BFS
        if not root:
            return 'null'
        
        q = deque([root])
        ser = []

        while q:
            curr = q.popleft()
            if not curr:
                ser.append("null")
            else:
                ser.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)

        return ','.join(ser)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # preprocess
        datasplit = data.split(',')

        if datasplit[0] == 'null':
            return None
        
        root = TreeNode(int(datasplit[0]))
        q = deque([root])
        i = 1

        while q:
            curr = q.popleft()
            lc,rc = datasplit[i], datasplit[i+1]
            i+=2

            if lc != 'null':
                curr.left = TreeNode(int(lc))
                q.append(curr.left)
            if rc != 'null':
                curr.right = TreeNode(int(rc))
                q.append(curr.right)

        return root