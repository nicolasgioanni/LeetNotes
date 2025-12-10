class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()

        for node, neighbor in edges:
            adjList[node].append(neighbor)
            adjList[neighbor].append(node)

        def dfs(node, prevNode, path):   
            if node in path:
                return False
            
            path.add(node)
            
            for neighbor in adjList[node]:
                if neighbor != prevNode:
                    if not dfs(neighbor, node, path):
                        return False

            return True
        
        return dfs(0, -1, visited) and len(visited) == n
