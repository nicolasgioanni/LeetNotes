# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        
        def inorder(node, count):
            nonlocal result
            if count == k: return count
            elif not node: return count

            count = inorder(node.left, count) + 1
            if count == k:
                result = node.val
                return count

            count = inorder(node.right, count)
            return count

        inorder(root, 0)
        return result
