class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        if s[0] == '0':
            return 0
        dp[1] = 1
        prev = int(s[0])

        for i in range(2, n+1):
            s_num = int(s[i-1])
            if s_num == 0:
                if prev == 0 or prev > 2:
                    return 0
                dp[i] = dp[i-2]
            else:
                if prev == 1 or (prev == 2 and s_num <= 6):
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            prev = s_num
        
        print(dp)
        return dp[n]