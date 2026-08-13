# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

NULL = 'null'
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return NULL

        # Level Order Traversal, NONE for no child
        res = []
        q = deque()
        q.append(root)
        res.append(str(root.val))

        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                res.append(str(curr.left.val))
            else:
                res.append(NULL)

            if curr.right:
                q.append(curr.right)
                res.append(str(curr.right.val))
            else:
                res.append(NULL)
        res = ','.join(res)
        print(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == NULL:
            return None

        tree = data.split(',')
        idx = 0
        root = TreeNode(tree[idx])
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            idx+=1
            if tree[idx] != NULL:
                lnode = TreeNode(tree[idx])
                curr.left = lnode
                q.append(lnode)
            idx+=1
            if tree[idx] != NULL:
                rnode = TreeNode(tree[idx])
                curr.right = rnode
                q.append(rnode)

        return root

            