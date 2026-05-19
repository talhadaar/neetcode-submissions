# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def min(self, root: Optional[TreeNode]):
        current = root
        while current and current.left:
            current = current.left
        return current
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # if has only 1 child, bring that up a level
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # if it has both children, find the min node in right subtree
            # level it up, and delete it
            else:
                minNode = self.min(root.right)
                root.val = minNode.val
                # delete min node, and attach its right subtree, to root's right subtree
                root.right = self.deleteNode(root.right, minNode.val)
        return root
            