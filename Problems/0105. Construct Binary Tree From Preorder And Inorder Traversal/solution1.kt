# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inIndexMap = {value: index for index, value in enumerate(inorder)}

        def recurse(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight or inLeft > inRight:
                return None
            else:
                
                rootVal = preorder[preLeft]
                root = TreeNode(rootVal)
                rootIndex = inIndexMap[rootVal]

                leftHalf = rootIndex - inLeft

                root.left = recurse(preLeft + 1, preLeft + leftHalf, inLeft, rootIndex - 1)
                root.right = recurse(preLeft + 1 + leftHalf, preRight, rootIndex + 1, inRight)

                return root

        return recurse(0, len(preorder) - 1, 0, len(inorder) - 1)
