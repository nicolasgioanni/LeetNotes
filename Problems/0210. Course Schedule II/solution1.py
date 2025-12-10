class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        visited = set()
        adjList = {}

        for node, neighbor in prerequisites:
            adjList.setdefault(node, []).append(neighbor)

        def dfs(node, path):
            if node in path:
                return False
            elif node in visited:
                return True
            else:
                if node in adjList:
                    path.add(node)
                    for neighbor in adjList[node]:
                        if not dfs(neighbor, path):
                            return False
                    path.remove(node)
        
                visited.add(node)
                result.append(node)
                return True

        for n in range(numCourses):
            if not dfs(n, set()):
                return []

        return result
