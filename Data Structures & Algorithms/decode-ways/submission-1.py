class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * 2 for _ in range(n+1)]
        dp[0][0] = 1
        dp[0][1] = 0
        prev = 10

        for i in range(1, n+1):
            s_num = int(s[i-1])
            if s_num == 0:
                if prev > 2:
                    return 0
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]
            else:
                if prev == 0:
                    dp[i][0] = dp[i-1][1]
                    dp[i][1] = 0
                elif prev == 1 or (prev == 2 and s_num <= 6):
                    dp[i][0] = dp[i-1][0] + dp[i-1][1]
                    dp[i][1] = dp[i-1][0]
                else:
                    dp[i][0] = dp[i-1][0] + dp[i-1][1]
                    dp[i][1] = 0
            prev = s_num
        
        print(dp)
        return sum(dp[n])