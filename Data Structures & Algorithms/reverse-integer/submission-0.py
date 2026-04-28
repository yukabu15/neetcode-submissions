class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x_str[0] == '-':
            res_str = x_str[0] + "".join(reversed(x_str[1:]))
            res = int(res_str)
            if res < -(1 << 31):
                return 0
        else:
            res_str = "".join(reversed(x_str))
            res = int(res_str)
            if res > (1 << 31) - 1:
                return 0
            
        return res