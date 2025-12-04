# Python Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = prices[0]

        for r in range(1, len(prices), 1):
            l = min(l, prices[r])
            result = max(result, prices[r] - l)

        return result
