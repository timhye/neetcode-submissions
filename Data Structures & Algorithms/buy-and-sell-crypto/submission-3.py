class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,0
        maxP = -1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            
            r += 1
            if r < len(prices):
                profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

        return maxP
        


            