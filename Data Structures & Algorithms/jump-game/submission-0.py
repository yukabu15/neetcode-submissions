class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(i+1, min(n, i+1+nums[i])):
                    dp[j] = True

        return dp[n-1]