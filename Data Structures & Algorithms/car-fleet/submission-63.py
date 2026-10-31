class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        for i in range(len(position)):
            while stk and stk[-1] <= ((target - position[i])/speed[i]):
                stk.pop()
            

            stk.append((target - position[i])/speed[i])
        
        return len(stk)

