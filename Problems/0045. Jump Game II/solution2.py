# BFS Exponential Time + Linear Space
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add(0)

        while queue:
            for i in range(len(queue)):
                index, jumps = queue.popleft()

                for j in range(index + 1, index + nums[index] + 1):
                    if j >= len(nums) - 1:
                        return jumps + 1
                    elif j not in visited:
                        visited.add(j)
                        queue.append((j, 1 + jumps))
