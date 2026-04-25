class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            if total > target:
                return
            
            for j in range(i, len(nums)):
                current.append(nums[j])
                dfs(j, current, total+nums[j])
                current.pop()
        
        res = []
        current = []
        dfs(0, current, 0)
        return res