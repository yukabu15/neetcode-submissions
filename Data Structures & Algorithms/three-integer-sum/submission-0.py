class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = (-1) * nums[i]
            l, r = i+1, n-1

            while l < r:
                if l != i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r != n-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                cand = nums[l] + nums[r]

                if cand == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -+ 1
                elif cand < target:
                    l += 1
                else:
                    r -= 1
        
        return ans

                    