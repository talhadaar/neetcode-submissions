# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = []

        def preorder(root, buff):
            if not root:
                buff.append("N")
                return
            buff.append(str(root.val))
            preorder(root.left, buff)
            preorder(root.right, buff)

        preorder(root, tree)
        return ",".join(tree)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def preorder():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder()