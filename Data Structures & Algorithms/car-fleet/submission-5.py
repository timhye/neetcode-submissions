class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        count = 1
        cars = [(pos,spd) for pos,spd in zip(position,speed)]
        cars.sort()
        print(cars)
        gate = (target - cars[-1][0]) / cars[-1][1]
        print(gate)
        for i in range(len(cars) - 1, -1, -1):
            if (target - cars[i][0]) / cars[i][1] <= gate:
                continue
            else:
                gate = (target - cars[i][0]) / cars[i][1]
                count += 1
        
        return count

             