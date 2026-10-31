class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                index = stk.pop()
                res[index] = (i - index)

            stk.append(i)
        
        return res