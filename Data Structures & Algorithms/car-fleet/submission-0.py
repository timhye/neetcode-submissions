class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i in range(len(position)):
            car.append((position[i],speed[i]))
        
        car.sort(key=lambda x:x[0])
        count = 0
        while car:
            gate = car.pop()
            time = (target - gate[0]) / gate[1]
            while car and ((target - car[-1][0]) / car[-1][1]) <= time:
                car.pop()
            count += 1
        
        return count

            
