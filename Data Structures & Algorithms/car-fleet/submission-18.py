class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        fleet = 0
        hold = sorted(zip(position, speed), reverse=True)
        print(hold)
        time = -1
        return
