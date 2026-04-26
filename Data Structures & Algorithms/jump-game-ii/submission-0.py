class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(n):
            if dp[i] or i == 0:
                for j in range(i+1, min(n, i+1+nums[i])):
                    if dp[j]:
                        dp[j] = min(dp[j], dp[i] + 1)
                    else:
                        dp[j] = dp[i] + 1

        print(dp)
        return dp[n-1]