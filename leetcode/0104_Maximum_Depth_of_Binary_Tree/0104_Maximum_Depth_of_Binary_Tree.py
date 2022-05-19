# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # excepotion
        if root == None:
            return 0
        # dfs (stack)
        stack = collections.deque([(root, 1)]) # (root, count)
        max_depth = 0
        while stack:
            root, count = stack.pop()
            if root.left == None or root.right == None:
                if count > max_depth:
                    max_depth = count
            if root.left != None:
                stack.append((root.left, count + 1))
            if root.right != None:
                stack.append((root.right, count + 1))
                
        return max_depth
        