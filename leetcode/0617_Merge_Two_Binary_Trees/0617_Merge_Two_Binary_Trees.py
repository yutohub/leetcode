# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        root1.val += root2.val
        # left
        root1.left = self.mergeTrees(root1.left, root2.left)
        # right
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
        