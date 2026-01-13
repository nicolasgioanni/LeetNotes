# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        
        def traverse(node):
            subTree = False
            if node == None:
                return False
            elif node.val == subRoot.val:
                subTree = isSame(node.left, subRoot.left) and isSame(node.right, subRoot.right)
            
            return traverse(node.left) or traverse(node.right) or subTree

        def isSame(node, subNode):
            if not node and not subNode:
                return True
            elif node and subNode and node.val == subNode.val:
                return isSame(node.left, subNode.left) and isSame(node.right, subNode.right)
            else:
                return False

        return traverse(root)
