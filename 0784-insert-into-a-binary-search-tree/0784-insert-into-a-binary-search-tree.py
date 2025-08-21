# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)   # empty tree case

        tempRoot = root

        while True:
            if(val < root.val):
                if(root.left):
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            else:
                if(root.right):
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break

        return tempRoot 

