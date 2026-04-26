class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        if ans <= 0:
            return ans
        n = len(nums)
        idx = 0
        cur_sum = 0
        while idx < n:
            if cur_sum + nums[idx] < 0:
                cur_sum = 0
            else:
                cur_sum += nums[idx]
            ans = max(ans, cur_sum)
            idx += 1

        ans = max(ans, cur_sum)

        return ans