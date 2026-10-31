class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [((target - position[i]) / speed[i]) for i in range(len(position))]
        fleet = 1
        for i in range(1,len(stk)):
            if stk[i] < stk[i - 1]:
                fleet += 1


        return fleet 


