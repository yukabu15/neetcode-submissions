class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        num_freq = []
        for num, count in num_count.items():
            num_freq.append([count, num])

        num_freq.sort(reverse=True)
        ans = []

        for i in range(k):
            ans.append(num_freq[i][1])
        
        return ans