class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adjacencyList = {node: set() for node in range(n)}

        for node, neighbor in edges:
            adjacencyList[node].add(neighbor)
            adjacencyList[neighbor].add(node)

        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjacencyList[node]:
                if prevNode == neighbor:
                    continue
                elif not dfs(neighbor, node):
                    return False
            return True
            
        return dfs(0, -1) and len(visited) == n
