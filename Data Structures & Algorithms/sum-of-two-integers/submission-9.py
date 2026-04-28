class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        c = 0
        max_int = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            print(i, a_bit, b_bit)
            xor = a_bit ^ b_bit
            s = xor ^ c
            print(i, s)
            c = (a_bit & b_bit) | (a_bit & c) | (b_bit & c)
            print(i, c)
            if s:
                ans |= (1 << i)

        if ans > max_int:
            ans = ~(ans ^ mask)
        
        return ans