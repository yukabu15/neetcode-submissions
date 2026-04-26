class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_idx = 0
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(0, n):
                if s[i] == s[j] and (j-i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        max_idx = i
                

        return s[max_idx:max_idx+max_len]