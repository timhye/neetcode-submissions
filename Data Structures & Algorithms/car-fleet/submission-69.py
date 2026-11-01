class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        process = [(i,v) for i, v in zip(position, speed)]
        process.sort()
        for i,v in process:
            while stk and stk[-1] <= ((target - i) / v):
                stk.pop()

            stk.append((target - i) / v)

        return len(stk)
        