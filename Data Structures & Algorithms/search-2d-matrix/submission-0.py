class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full_list = []
        for i in range(len(matrix)):
            full_list.extend(matrix[i])

        l = 0
        r = len(full_list) - 1

        while l <= r:
            m = l + (r - l) // 2
            if full_list[m] == target:
                return True
            elif full_list[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False