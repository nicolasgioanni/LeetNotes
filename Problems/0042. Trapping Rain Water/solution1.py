# Python
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if height[l] > height[r]:
                r -= 1

                if height[r] > maxR:
                    maxR = height[r]
                elif maxR - height[r] > 0:
                    result += maxR - height[r]
            else:
                l += 1

                if height[l] > maxL:
                    maxL = height[l]
                elif maxL - height[l] > 0:
                    result += maxL - height[l]

        return result
