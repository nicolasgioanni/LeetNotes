# Linear Time + Space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        ways = [0] * (n+1)

        ways[n] = 1
        ways[n - 1] = 1

        for i in range(n - 2, -1, -1):
            ways[i] = ways[i + 1] + ways[i + 2]

        return ways[0]
