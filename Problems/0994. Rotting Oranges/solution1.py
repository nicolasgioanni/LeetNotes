class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = collections.deque()
        freshFruits = 0
        totalTime = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    freshFruits += 1

        while queue:
            row, col, time = queue.popleft()

            for dr, dc in directions:
                checkRow, checkCol = row + dr, col + dc

                if (0 <= checkRow < rows and
                    0 <= checkCol < cols and
                    grid[checkRow][checkCol] == 1):
                    freshFruits -= 1
                    grid[checkRow][checkCol] = 2
                    queue.append((checkRow, checkCol, time + 1))
                    totalTime = max(totalTime, time + 1)

        return totalTime if freshFruits == 0 else -1
