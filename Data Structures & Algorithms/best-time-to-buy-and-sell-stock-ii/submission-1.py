class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell, buy = 0, 0
        while buy < len(prices):
            if prices[buy] <= prices[sell]:
                sell = buy
            
            else:
                profit += prices[buy] - prices[sell]
                sell = buy
            
            buy += 1
        
        return profit


