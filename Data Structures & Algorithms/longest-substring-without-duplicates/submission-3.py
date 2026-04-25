class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        char_idx = {}

        while r < len(s):
            if s[r] in char_idx and char_idx[s[r]] >= l:
                l = char_idx[s[r]] + 1
            max_len = max(max_len, r - l + 1)
            char_idx[s[r]] = r
            
            r += 1
        
        return max_len