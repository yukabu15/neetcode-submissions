class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rev_stones = [-stone for stone in stones]
        heapq.heapify(rev_stones)

        while len(rev_stones) > 1:
            x = heapq.heappop(rev_stones)
            x = -x
            y = heapq.heappop(rev_stones)
            y = -y
            if x > y:
                heapq.heappush(rev_stones, -(x - y))
            
        if rev_stones:
            return -rev_stones[0]
        else:
            return 0