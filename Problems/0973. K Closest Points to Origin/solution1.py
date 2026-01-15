class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidean(first, second):
            x1, y1 = first
            x2, y2 = second

            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            return distance
        
        target = (0, 0)

        for i in range(len(points)):
            points[i] = [euclidean(target, points[i])] + points[i]

        heapq.heapify(points)

        result = []
        for i in range(k):
            distance, x, y = points[0]
            result.append([x, y])
            heapq.heappop(points)

        return result
