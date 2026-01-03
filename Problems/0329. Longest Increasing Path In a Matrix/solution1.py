# DP Optimal Time + Space, O(r * c)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(matrix), len(matrix[0])
        longest = 0
        dp = {}

        def dfs(row, col):
            if (row, col) in dp:
                return dp[(row, col)]

            dp[(row, col)] = 1
            for dr, dc in directions:
                checkRow, checkCol = row + dr, col + dc

                if (0 <= checkRow < rows and
                    0 <= checkCol < cols and
                    matrix[checkRow][checkCol] > matrix[row][col]):
                    dp[(row, col)] = max(dp[(row, col)], 1 + dfs(checkRow, checkCol))
            
            return dp[(row, col)]

        for row in range(rows):
            for col in range(cols):
                longest = max(longest, dfs(row, col))

        return longest
