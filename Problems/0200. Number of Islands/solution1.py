class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]] # Move left, right, up, down
        islands = 0
        visited = set() # Row, Col

        def bfs(row, col):
            visited.add((row, col))
            
            queue = collections.deque()
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    checkRow, checkCol = row + dr, col + dc

                    if (0 <= checkRow < rows and
                        0 <= checkCol < cols and
                        grid[checkRow][checkCol] == "1" and
                        (checkRow, checkCol) not in visited):
                        visited.add((checkRow, checkCol))
                        queue.append((checkRow, checkCol))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands
