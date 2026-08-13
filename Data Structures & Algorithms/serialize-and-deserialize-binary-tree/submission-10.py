# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# USING DFS with preorder traversal
NULL = 'null'
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append(NULL)
                return None

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res = ','.join(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == NULL:
            return None

        tree = data.split(',')
        self.idx = 0

        def dfs():
            if tree[self.idx] == NULL:
                self.idx+=1
                return None

            node = TreeNode(int(tree[self.idx]))
            self.idx+=1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

            