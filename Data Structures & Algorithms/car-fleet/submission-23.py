class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        fleet = 0
        for i in range(len(position) - 1,-1,-1):
            while stk and stk[-1] >= ((target - position[i]) / 2):
                stk.pop()
                
            
            stk.append(i)
            fleet += 1
        return fleet

