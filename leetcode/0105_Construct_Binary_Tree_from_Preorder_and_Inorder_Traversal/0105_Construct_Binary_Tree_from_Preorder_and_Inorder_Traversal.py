# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # exception
        if not preorder or not inorder:
            return None
        # get root from preorder
        root = TreeNode(preorder[0])
        # divide into right and left tree
        mid = inorder.index(preorder[0])
        
        # give new preorder
        # root, left, right
        # preorder[0], preorder[1:mid+1], preorder[mid+1:]
        
        # give new inorder
        # left, root, right
        # inorder[:mid], inorder[mid], inorder[mid+1:]
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        