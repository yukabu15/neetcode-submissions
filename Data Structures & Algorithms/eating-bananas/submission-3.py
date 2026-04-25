class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        ans = 10**9+1

        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for i in range(n):
                time += math.ceil(piles[i] / m)
            if time <= h:
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1

        return ans