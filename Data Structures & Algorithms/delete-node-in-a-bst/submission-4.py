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


        parent, cur = None, root

        while cur: 
            if key > cur.val:
                parent = cur
                cur = cur.right
            elif key < cur.val:
                parent = cur
                cur = cur.left
            else:
                if not cur.left or not cur.right:
                    child = cur.left if cur.left else cur.right
                    if not parent:
                        return child
                    if parent.left == cur:
                        parent.left = child
                        return root
                    else:
                        parent.right = child
                        return root
                else:
                    def findAndDeleteMin(root, child):
                        parent, cur = root, child
                        while cur.left:
                            parent = cur
                            cur = cur.left
                        if parent == root:
                            parent.right = cur.right
                        else:
                            parent.left = cur.right
                        return cur.val
                        
                    cur.val = findAndDeleteMin(cur, cur.right)
                    return root
        
        return root
