# Brute Force
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(step):
            if step > n:
                return 0
            elif step < n:
                return dfs(step + 1) + dfs(step + 2)
            else:
                return 1

        return dfs(0)
