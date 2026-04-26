class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            cur = 0
            for j in range(32):
                if i & 1 << j:
                    cur += 1
            ans.append(cur)

        return ans
