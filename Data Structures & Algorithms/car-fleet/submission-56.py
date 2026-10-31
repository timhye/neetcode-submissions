class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        arr = sorted([(position[i], (target- position[i])/speed[i]) for i in range(len(position))], reverse=True)
        fleet = 1
        for i in range(len(arr)):
            if stk and stk[-1] < arr[i][1]:
                fleet += 1
                continue
                
            stk.append(arr[i][1])
        return fleet
