# Python Two-pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = 0

        for r in range(1, len(prices), 1):
            if prices[l] > prices[r]:
                l = r
            else:
                result = max(result, prices[r] - prices[l])

        return result
