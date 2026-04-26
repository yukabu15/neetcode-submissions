class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = nums[0]
        dp[0][1] = max(nums[0], nums[1])
        dp[1][1] = nums[1]
        dp[1][2] = max(nums[1], nums[2])

        for i in range(2):
            for j in range(2+i, n-1+i):
                dp[i][j] = max(dp[i][j-1], dp[i][j-2] + nums[j])

        return max(dp[0][n-2], dp[1][n-1])