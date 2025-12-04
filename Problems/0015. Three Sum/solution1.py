# Python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        target = 0
        nums.sort()

        for i, n in enumerate(nums):
            if n > target:
                break
            
            if i > 0 and nums[i - 1] == n:
                continue

            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
                else:
                    results.append([n, nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
        return results
