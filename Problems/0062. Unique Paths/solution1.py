# Brute Force
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0, 1), (1, 0)]
        
        def dfs(row, col, path):
            if row == m - 1 and col == n - 1:
                return 1

            path.add((row, col))
            paths = 0
            
            for dr, dc in directions:
                checkRow, checkCol = row + dr, col + dc

                if (0 <= checkRow < m and
                    0 <= checkCol < n and
                    (checkRow, checkCol) not in path):
                    paths += dfs(checkRow, checkCol, path)

            path.remove((row, col))
            return paths


        return dfs(0, 0, set())
