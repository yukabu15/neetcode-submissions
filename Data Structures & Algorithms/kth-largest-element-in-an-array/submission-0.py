class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_nums = [-num for num in nums]
        heapq.heapify(rev_nums)

        for _ in range(k):
            ans = heapq.heappop(rev_nums)
            ans = -ans

        return ans
