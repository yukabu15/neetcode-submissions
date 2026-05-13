class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_cur = 1
        prefix_prod = [prefix_cur]
        for i in range(n-1):
            prefix_cur *= nums[i]
            prefix_prod.append(prefix_cur)
        
        suffix_cur = 1
        suffix_prod = [suffix_cur]
        for i in range(n-1, 0, -1):
            suffix_cur *= nums[i]
            suffix_prod.append(suffix_cur)
        
        suffix_prod.reverse()

        ans = []
        for i in range(n):
            ans.append(prefix_prod[i] * suffix_prod[i])
        
        return ans