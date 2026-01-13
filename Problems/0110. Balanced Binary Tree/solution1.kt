# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node == None:
                return 0

            leftDepth, rightDepth = dfs(node.left), dfs(node.right)
            if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
                return -1
            else:
                return 1 + max(leftDepth, rightDepth)

        return dfs(root) != -1
