# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Calculate max diameter in nodes then adjust to edges
        
        def dfs(node):
            if node == None:
                return 0, 0

            leftLength, leftMax = dfs(node.left)
            rightLength, rightMax = dfs(node.right)

            currLength = 1 + max(leftLength, rightLength)
            currMax = max(leftLength + rightLength + 1, leftMax, rightMax)

            return (currLength, currMax)

        return dfs(root)[1] - 1
