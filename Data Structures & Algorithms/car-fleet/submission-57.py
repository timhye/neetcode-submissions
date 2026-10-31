class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted([(position[i], (target- position[i])/speed[i]) for i in range(len(position))], reverse=True)
        time = -1
        fleet = 1
        for i in range(len(arr)):
            if arr[i][1] > time:
                fleet += 1
                time = arr[i][1]
            
        return fleet

