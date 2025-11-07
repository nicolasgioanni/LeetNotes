class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        chestCoordinate = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    chestCoordinate.add((row, col))

        queue = collections.deque()
        for treasureRow, treasureCol in chestCoordinate:
            queue.append((treasureRow, treasureCol))

        while queue:
            currentRow, currentCol = queue.popleft()

            for dr, dc in directions:
                checkRow = dr + currentRow
                checkCol = dc + currentCol

                if (0 <= checkRow < rows and
                    0 <= checkCol < cols and
                    grid[checkRow][checkCol] == 2147483647):

                    grid[checkRow][checkCol] = grid[currentRow][currentCol] + 1
                    queue.append((checkRow, checkCol))
