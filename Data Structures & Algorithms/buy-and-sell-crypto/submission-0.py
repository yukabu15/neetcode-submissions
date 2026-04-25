class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        max_num = [prices[n-1] for _ in range(n)]
        min_num = [prices[0] for _ in range(n)]
        for i in range(1, n):
            min_num[i] = min(min_num[i-1], prices[i-1])
            max_num[n-i-1] = max(max_num[n-i], prices[n-i])
        
        for i in range(n):
            ans = max([ans, max_num[i] - prices[i], prices[i] - min_num[i]])
        
        return ans
