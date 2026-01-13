# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        queue = collections.deque()
        if root: queue.append(root)

        while queue:
            levelLength = len(queue)

            for i in range(levelLength):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i + 1 == levelLength: result.append(node.val)

        return result
