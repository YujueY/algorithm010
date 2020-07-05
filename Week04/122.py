class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices) - 1):
            temp = prices[i + 1] - prices[i]
            if temp > 0:
                profit = profit + temp
        return profit
