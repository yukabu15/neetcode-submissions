class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = dict()
        for num in nums:
            if num in visited:
                return True
            else:
                visited[num] = 1
        
        return False