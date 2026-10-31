class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [((position[i],(target - position[i]) / speed[i])) for i in range(len(position))]
        stk.sort(reverse=True)
        time = -1
        fleet = 1
        for i in range(len(stk)):
            if stk[i][1] > time:
                time = stk[i][1]
            
            fleet += 1


        return fleet


