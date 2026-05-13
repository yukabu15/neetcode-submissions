class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        num_frequency = []
        for key, value in num_count.items():
            num_frequency.append([value, key])

        num_frequency.sort(reverse=True)

        ans = [num[1] for num in num_frequency[:k]]
        return ans