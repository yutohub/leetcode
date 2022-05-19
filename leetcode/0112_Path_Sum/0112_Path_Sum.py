# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        # exception
        if not root:
            return False
        # dfs (stack)
        stack = collections.deque([(root, root.val)])
        while stack:
            root, count = stack.pop()
            if root.left == None and root.right == None and count == targetSum:
                return True
            if root.left != None:
                stack.appendleft((root.left, count + root.left.val))
            if root.right != None:
                stack.appendleft((root.right, count + root.right.val))
        else:
            return False