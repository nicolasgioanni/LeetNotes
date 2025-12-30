class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        sumSet = set()
        sumSet.add(0)
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            iterateSet = set(sumSet)
            for sums in iterateSet:
                sumSet.add(sums + n)
                if sums + n <= target: dp[sums + n] = dp[sums]

        return dp[target]
