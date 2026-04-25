class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1

        if zero_count >= 2:
            return [0 for i in range(n)]
        elif zero_count == 1:
            ans = []
            max_product = 1
            for num in nums:
                if num != 0:
                    max_product *= num
            for num in nums:
                if num == 0:
                    ans.append(max_product)
                else:
                    ans.append(0)
        else:
            ans = []
            max_product = 1
            for num in nums:
                max_product *= num
            for num in nums:
                ans.append(max_product//num)
        
        return ans