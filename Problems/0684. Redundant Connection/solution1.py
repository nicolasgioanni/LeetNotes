class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList, queue, path = defaultdict(list), collections.deque(), set()

        for node, neighbor in edges:
            adjList[node].append(neighbor)
            adjList[neighbor].append(node)

        def dfs(node, prevNode):
            if node in path:
                while queue[0] != node:
                    pastNode = queue.popleft()
                    path.remove(pastNode)
                return True

            path.add(node)
            queue.append(node)

            for neighbor in adjList[node]:
                if neighbor != prevNode and dfs(neighbor, node):
                    return True
            
            queue.pop()
            path.remove(node)
            return False

        dfs(edges[0][0], -1)

        for node, neighbor in edges[::-1]:
            if node in path and neighbor in path:
                return [node, neighbor]
