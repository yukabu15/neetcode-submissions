class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell = []
        min_sell.append(prices[0])
        maxP = 0

        for i in range(1, len(prices)):
            maxP = max(maxP, prices[i] - min_sell[i-1])
            min_sell.append(min(min_sell[i-1], prices[i]))
        
        return maxP