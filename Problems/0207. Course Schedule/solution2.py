class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()

        for node, neighbor in prerequisites:
            adjList[node].append(neighbor)

        def dfs(node, path):
            if node in visited or not adjList[node]:
                return True
            if node in path:
                return False

            path.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor, path):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True

        for n in range(numCourses):
            if not dfs(n, set()):
                return False
        
        return True
