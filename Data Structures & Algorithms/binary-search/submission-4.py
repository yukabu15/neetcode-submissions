class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n
        prev = 100000

        while l < r:
            half = l + (r - l) // 2
            if prev == half:
                break
            if nums[half] == target:
                return half
            elif nums[half] < target:
                l = half
            else:
                r = half
            prev = half
        
        return -1
