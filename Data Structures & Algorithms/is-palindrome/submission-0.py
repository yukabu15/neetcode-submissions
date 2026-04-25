class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = "".join([char.lower() if char.isalnum() else "" for char in s])
        l = 0
        r = len(valid_s)-1
        
        while l < r:
            if valid_s[l] != valid_s[r]:
                return False
            else:
                l += 1
                r -= 1 
        
        return True