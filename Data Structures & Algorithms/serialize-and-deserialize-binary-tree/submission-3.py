# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Level order traversal
        if not root:
            return "N"

        queue = [root]
        res = []

        while queue:
            top = queue.pop(0)
            if not top:
                res.append("N")
            else:
                res.append(str(top.val))
                queue.append(top.left)
                queue.append(top.right)
        return ",".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        self.i = 1
        queue = [root]

        while queue:
            top = queue.pop(0)
            if vals[self.i] != "N":
                top.left = TreeNode(int(vals[self.i]))
                queue.append(top.left)
            self.i +=1
            if vals[self.i] != "N":
                top.right = TreeNode(int(vals[self.i]))
                queue.append(top.right)
            self.i += 1
        
        return root