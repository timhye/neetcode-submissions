class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        lowest = 0
        while left <= right:
            mid = left + (right - left) // 2
            day = 0
            amt = 0
            i = 0
            while i < len(weights):
                check = amt + weights[i]
                if check == mid:
                    day += 1
                    amt = 0
                elif check < mid:
                    amt = check
                else:
                    day += 1
                    amt = weights[i]

                i += 1
            
        
            if day > days:
                left = mid + 1
            
            elif day <= days:
                lowest = mid
                right = mid - 1
            
        return lowest

                


                

            

                



