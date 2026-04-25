class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        ans = 0

        while l < r:
            if heights[l] <= heights[r]:
                cand = (r-l) * heights[l]
                ans = max(cand, ans)
                l += 1
            elif heights[l] > heights[r]:
                cand = (r-l) * heights[r]
                ans = max(cand, ans)
                r -= 1
        
        return ans