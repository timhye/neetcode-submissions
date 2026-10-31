class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [((position[i],(target - position[i]) / speed[i])) for i in range(len(position))]
        
        stk.sort()
        fleet = 1
        for i in range(len(position) - 2, 0, -1):
            if stk[i+ 1][1] > stk[i][1]:
                fleet += 1


        return fleet


