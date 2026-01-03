#DP Optimal Time + Space, O(n * s)/O(s)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        row = defaultdict(int) # sums : counts
        row[0] = 1

        for n in nums:
            currentRow = defaultdict(int)
            for prevSum, count in row.items():
                currentRow[prevSum + n] += count
                currentRow[prevSum - n] += count
            row = currentRow

        return row[target]
