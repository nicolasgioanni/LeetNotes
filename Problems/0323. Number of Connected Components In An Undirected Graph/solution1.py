# Recursive Depth First Search
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {node: set() for node in range(n)}
        
        for node, neighbor in edges:
            adjacencyList[node].add(neighbor)
            adjacencyList[neighbor].add(node)

        visited = set()
        components = 0

        def dfs(node):
            for neighbor in adjacencyList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                components += 1
                visited.add(node)
                dfs(node)
        
        return components
