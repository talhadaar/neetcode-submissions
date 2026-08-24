class Solution:
    def min(self, root: Optional[TreeNode]):
        current = root
        while current and current.left:
            current = current.left
        return current
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # traverse and find the key to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # key was found
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            # whoops - has both children
            # We will find the minimum
            else:
                minChild = self.min(root.right)
                root.val = minChild.val
                root.right = self.deleteNode(root.right, minChild.val)
        return root