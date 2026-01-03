# DP Top-Down
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i + j == len(s3):
                return True

            if len(s1) > i and len(s2) > j and s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                dp[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
            elif len(s1) > i and s1[i] == s3[i + j]:
                dp[(i, j)] = dfs(i + 1, j)
            elif len(s2) > j and s2[j] == s3[i + j]:
                dp[(i, j)] = dfs(i, j + 1)
            else:
                dp[(i, j)] = False

            return dp[(i, j)]

        return dfs(0, 0)
