# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root):        
        # exception
        if root == None:
            return 0
        # bfs(que)
        que = collections.deque([(root, 1)])
        while que:
            root, count = que.popleft()
            if root.left == None and root.right == None:
                return count
            # left
            if root.left != None:
                que.append((root.left, count + 1))
            # right
            if root.right != None:
                que.append((root.right, count + 1))
        return 0
        