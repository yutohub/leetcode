# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        # exception
        if root == None:
            return False
        # bfs (que)
        que = collections.deque([(root, -float(inf), float(inf))])
        while que:
            root, minimum, maximum = que.popleft()
            # parent parent < left child < parent
            if root.left != None:
                if minimum < root.left.val < root.val:
                    que.append((root.left, minimum, root.val))
                else:
                    return False
            # parent < right child < parent parent
            if root.right != None:
                if root.val < root.right.val < maximum:
                    que.append((root.right, root.val, maximum))
                else:
                    return False
        else:
            return True