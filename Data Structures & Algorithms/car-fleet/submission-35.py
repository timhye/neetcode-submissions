class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [((position[i],(target - position[i]) / speed[i])) for i in range(len(position))]
        
        stk.sort()
        print(stk)
        fleet = 1
        for i in range(1,len(stk)):
            if stk[i][1] < stk[i - 1][1]:
                fleet += 1


        return 


