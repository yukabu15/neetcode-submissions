class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_numbers = [[num, i] for i, num in enumerate(numbers, 1)]
        new_numbers.sort()
        n = len(numbers)
        l = 0
        r = n-1

        while l < r:
            sum_nums = new_numbers[l][0] + new_numbers[r][0]

            if sum_nums == target:
                return sorted([new_numbers[l][1], new_numbers[r][1]])
            elif sum_nums < target:
                l += 1
            else:
                r -= 1