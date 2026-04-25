from math import sqrt

class Solution:
    def distance(self, point: List[int]) -> float:
        x, y = point
        return sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_cand = [[self.distance(point), point] for point in points]
        heapq.heapify(point_cand)
        ans = []

        for _ in range(k):
            closest = heapq.heappop(point_cand)
            ans.append(closest[1])

        return ans 
