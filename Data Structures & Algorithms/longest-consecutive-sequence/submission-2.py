class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        nums.sort()
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                ans = max(ans, current)
                current = 1
        
        ans = max(ans, current)
        
        return ans
