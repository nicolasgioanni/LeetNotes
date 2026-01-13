# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(pNode, qNode):
            if pNode != None and qNode != None and pNode.val == qNode.val:
                return dfs(pNode.left, qNode.left) and dfs(pNode.right, qNode.right)
            elif pNode == qNode == None:
                return True
            else:
                return False

        return dfs(p, q)
