class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [1] * len(temperatures)
        stk.append(0)
        for i in range(len(temperatures)):

            while stk and temperatures[i] >= temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            
            stk.append(temperatures[i])

        return res

