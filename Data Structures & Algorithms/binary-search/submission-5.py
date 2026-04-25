class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            half = l + (r - l) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target:
                l = half+1
            else:
                r = half-1
            prev = half
        
        return -1
