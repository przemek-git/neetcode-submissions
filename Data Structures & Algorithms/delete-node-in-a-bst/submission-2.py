# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else: 
                def findMin(root: TreeNode):
                    cur = root
                    while cur:
                        if not cur.left:
                            return cur.val
                        cur = cur.left
                    return None
                minVal = findMin(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)

        return root