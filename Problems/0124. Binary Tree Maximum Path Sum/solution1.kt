# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node):
            if not node:
                return 0, float("-inf")
            else:
                leftDown, leftBest = recurse(node.left)
                rightDown, rightBest = recurse(node.right)

                leftDown = max(0, leftDown)
                rightDown = max(0, rightDown)

                down = node.val + max(leftDown, rightDown)
                best = max(leftBest, rightBest, node.val + leftDown + rightDown)

            return down, best

        return recurse(root)[1]
