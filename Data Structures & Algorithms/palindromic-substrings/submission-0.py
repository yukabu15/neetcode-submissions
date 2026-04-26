class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        n = len(s)
        def check(l, r):
            cur_length = 0
            while 0 <= l and r < n:
                if s[l] == s[r]:
                    self.ans += 1
                    l -= 1
                    r += 1
                else:
                    return

        for i in range(n):
            check(i, i)
            check(i, i+1)
        
        return self.ans