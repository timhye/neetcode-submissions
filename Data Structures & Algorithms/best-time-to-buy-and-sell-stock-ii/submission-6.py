class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        left = 0
        for right in range(len(prices)):
            
            if prices[right] >= prices[left]:
                mProfit += (prices[right] - prices[left])
                
            left = right

        return mProfit 