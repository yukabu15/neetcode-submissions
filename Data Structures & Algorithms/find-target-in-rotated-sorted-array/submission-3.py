class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            m = l + (r-l) // 2
            if target == nums[m]:
                return m
            if target == nums[r]:
                return r
            if target == nums[l]:
                return l
            if target < nums[m]:
                if target < nums[l] < nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1