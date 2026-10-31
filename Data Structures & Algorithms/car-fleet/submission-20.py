class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        fleet = 0
        hold = sorted(zip(position, speed), reverse=True)
        time = -1
        for el in hold:
            check = (target - el[0]) / el[1]
            if check > time:
                time = check
                fleet += 1
        return fleet

