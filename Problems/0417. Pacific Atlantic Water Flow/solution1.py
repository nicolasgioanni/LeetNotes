class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(heights), len(heights[0])
        results = []
        pacific, atlantic = set(), set()

        def dfs(row, col, oldHeight, visited):
            if (0 <= row < rows and
                0 <= col < cols and
                heights[row][col] >= oldHeight and
                (row, col) not in visited):
                visited.add((row, col))

                for dr, dc in directions:
                    checkRow, checkCol = dr + row, dc + col
                    dfs(checkRow, checkCol, heights[row][col], visited)

        for row in range(rows):
            dfs(row, 0, float("-inf"), pacific)
            dfs(row, cols - 1, float("-inf"), atlantic)

        for col in range(cols):
            dfs(0, col, float("-inf"), pacific)
            dfs(rows - 1, col, float("-inf"), atlantic)

        for (row, col) in pacific:
            if (row, col) in atlantic:
                results.append([row, col])

        return results
