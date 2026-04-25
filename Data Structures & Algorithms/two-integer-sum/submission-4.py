class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = [(num, i) for i, num in enumerate(nums)]
        nums_idx.sort()
        n = len(nums)

        for i in range(n-1):
            l = i
            r = n-1

            while l < r:
                total = nums_idx[l][0] + nums_idx[r][0]
                
                if total == target:
                    res = [nums_idx[l][1], nums_idx[r][1]]
                    res.sort()
                    return res
                elif total > target:
                    r -= 1
                else:
                    l += 1