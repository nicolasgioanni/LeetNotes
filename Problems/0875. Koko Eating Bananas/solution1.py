class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r 

        while l <= r:
            m = l + (r - l) // 2
            hours = 0

            for b in piles:
                hours += math.ceil(b / m)

            if hours <= h:
                r = m - 1
                result = m
            else:
                l = m + 1 

        return result
