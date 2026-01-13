# Same as solution 1 but a bit broken down
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}

        def recurse(preL, preR, inL, inR):
            if preL > preR or inL > inR:
                return None

            rootVal = preorder[preL]
            root = TreeNode(rootVal)
            inorderIndex = inorderMap[rootVal]

            LeftHalf = inorderIndex - inL

            root.left = recurse(preL + 1, preL + LeftHalf, inL, inorderIndex - 1)
            root.right = recurse(preL + 1 + LeftHalf, preR, inorderIndex + 1, inR)

            return root


        return recurse(0, len(preorder) - 1, 0, len(inorder) - 1)
