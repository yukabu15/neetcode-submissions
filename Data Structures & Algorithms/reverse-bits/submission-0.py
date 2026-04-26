class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n & 1 << i:
                place = 1
            else:
                place = 0
            ans += 2 ** (31-i) * place
        
        return ans