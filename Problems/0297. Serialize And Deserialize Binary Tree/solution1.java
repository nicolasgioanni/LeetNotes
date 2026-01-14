# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = collections.deque()
        if root: queue.append(root)
        result = []

        while queue:
            levelLength = len(queue)
            for i in range(levelLength):
                node = queue.popleft()
                if node: 
                    queue.append(node.left)
                    queue.append(node.right)

                result.append(str(node.val) if node else "!")

        for i in range(len(result) - 1, -1, -1):
            if result[i] == "!": result.pop()
            else: break

        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) > 0: tokens = data.split(",")
        else: return None

        root = TreeNode(int(tokens[0]))
        queue = collections.deque()
        queue.append(root)
        
        i = 1
        while queue:
            node = queue.popleft()

            if i < len(tokens) and tokens[i] != "!":
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1

            if i < len(tokens) and tokens[i] != "!":
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1

        return root
