class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        stk.append(temperatures[0])
        for i in range(len(temperatures)):

            while stk and temperatures[i] > stk[len(stk) - 1]:
                res[len(stk) - 1] = i - (len(stk) - 1)
                stk.pop()
            
            stk.append(temperatures[i])

        return res

