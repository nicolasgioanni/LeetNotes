# Iterative Breath First Search
# Can swap easily to Iterative DFS changing popleft to pop
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyMap = {node: set() for node in range(n)}
        for node, neighbor in edges:
            adjacencyMap[node].add(neighbor)
            adjacencyMap[neighbor].add(node)

        components = 0
        visited = set()

        def bfs(node):
            queue = collections.deque()
            queue.append(node)

            while queue:
                node = queue.popleft()
                for neighbor in adjacencyMap[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        for node in range(n):
            if node not in visited:
                components += 1
                visited.add(node)
                bfs(node)


        return components
