# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, pathMax):
            if not node:
                return 0  
            
            count = 1 if node.val >= pathMax else 0
            newMax = node.val if node.val > pathMax else pathMax

            return count + dfs(node.left, newMax) + dfs(node.right, newMax)

        return dfs(root, float('-inf'))
