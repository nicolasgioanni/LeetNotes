# Brute Force
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)) # insert, delete, replace

        return dfs(0, 0)
