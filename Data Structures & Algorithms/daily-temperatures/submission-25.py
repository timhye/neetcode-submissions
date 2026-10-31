class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                val = stk.pop()
                res[val] = i - val
            
            stk.append(i)
        return res