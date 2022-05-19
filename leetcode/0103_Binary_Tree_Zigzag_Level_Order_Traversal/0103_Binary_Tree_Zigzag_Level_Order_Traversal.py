# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        # exception
        if not root:
            return None
        # root, level
        levels = collections.defaultdict(list)
        que = collections.deque([(root, 1)])
        # bfs (que)
        while que:
            root, level = que.popleft()
            levels[level].append(root.val)
            if root.left != None:
                que.append((root.left, level + 1))
            if root.right != None:
                que.append((root.right, level + 1))
        # reverse
        for i, row in enumerate(levels.values()):
            if i % 2:
                row.reverse()
        return levels.values()
