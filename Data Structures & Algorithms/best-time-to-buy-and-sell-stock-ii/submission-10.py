class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for right in range(1,len(prices)):
            if prices[right] > prices[right - 1]:
                profit += (prices[right] - prices[right - 1])
                    
        return profit