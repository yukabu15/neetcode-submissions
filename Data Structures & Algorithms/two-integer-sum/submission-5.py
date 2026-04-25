class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in visited:
                return [visited[diff], i]
            else:
                visited[num] = i
