# Linear Time + Constant Space:
class Solution:
    def climbStairs(self, n: int) -> int:
        waysOne, waysTwo = 1, 1

        for i in range(n - 1):
            temp = waysOne
            waysOne = waysOne + waysTwo
            waysTwo = temp

        return waysOne
