class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []
        used = [False] * len(nums)
        
        def dfs():
            if len(current) == len(nums):
                ans.append(current.copy())
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                current.append(nums[i])

                dfs()

                current.pop()
                used[i] = False

        dfs()
        return ans