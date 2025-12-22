# Brute Force O(2^n)
class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            elif s[i] == "0":
                return 0

            result = dfs(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] < "7")):
                result += dfs(i + 2)

            return result

        return dfs(0) if s else 0
