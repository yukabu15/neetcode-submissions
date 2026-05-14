class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        num_dict = dict()
        ans = 0

        for num in nums:
            prev = num - 1
            if prev in num_dict:
                length = num_dict[prev] + 1
            else:
                length = 1
            num_dict[num] = length
            ans = max(length, ans)
            
        return ans