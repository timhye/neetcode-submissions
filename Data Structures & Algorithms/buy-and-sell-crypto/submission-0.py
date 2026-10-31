class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):                       
                sell = prices[j]
                newprofit = sell - buy
                if newprofit > high:
                    high = newprofit
        
        return high