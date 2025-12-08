class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        seen = set()
        islandArea = 0

        def dfs(row, col) -> int:
            seen.add((row, col))
            area = 1
            for dr, dc in directions:
                checkRow, checkCol = row + dr, col + dc

                if (0 <= checkRow < rows and
                    0 <= checkCol < cols and
                    (checkRow, checkCol) not in seen and
                    grid[checkRow][checkCol] == 1):
                    area += dfs(checkRow, checkCol)

            return area

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    islandArea = max(islandArea, dfs(row, col))

        return islandArea
