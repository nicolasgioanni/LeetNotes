# Brute Force
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i):
            if i == len(s):
                return True

            for word in wordDict:
                r = 0
                while i + r < len(s) and r < len(word) and s[i + r] == word[r]:
                    r += 1
                if r == len(word) and dfs(i + r):
                    return True

            return False

        return dfs(0)
