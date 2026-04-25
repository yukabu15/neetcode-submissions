class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i, current, total):
            if total == target:
                ans.append(current.copy())

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + total > target:
                    return
                
                current.append(candidates[j])
                dfs(j+1, current, total + candidates[j])
                current.pop()

        
        dfs(0, [], 0)

        return ans
