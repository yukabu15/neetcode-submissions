class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]


        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[n-1-i] = suffix[n-i] * nums[n-i]
        
        ans = []
        for i in range(n):
            ans.append(prefix[i]*suffix[i])

        return ans