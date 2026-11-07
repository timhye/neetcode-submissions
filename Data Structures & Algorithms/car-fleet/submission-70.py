class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        orderd = [(position[i], (target - position[i])/ speed[i]) for i in range(len(position))]
        orderd.sort()
        for el in orderd:
            while stk and stk[-1][1] <= el[1]:
                stk.pop()
            
            stk.append(el)
        
        return len(stk)

