class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        stk = []
        count = 0
        cars = [(pos,spd) for pos,spd in zip(position,speed)]
        cars.sort(reverse=True)
        for car in cars:
            time = (target - car[0]) / car[1]
            if stk and stk[-1] >= time:
                continue

            count += 1
            stk.append(time)
        
        return count


             