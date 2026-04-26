class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.ans = ""
        self.max_length = 0
        n = len(s)
        def check(l, r):
            cur_length = 0
            while 0 <= l and r < n:
                if s[l] == s[r]:
                    if (r-l+1) > self.max_length:
                        self.max_length = r-l+1
                        self.ans = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    return

        for i in range(n):
            check(i, i)
            check(i, i+1)
        
        return self.ans