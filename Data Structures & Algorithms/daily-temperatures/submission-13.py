class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stk:
                stk.append(i)
            else:
                while stk and temperatures[i] > temperatures[stk[-1]]:
                    res[stk[-1]] = i - stk[-1][1]
                    stk.pop()

                stk.append(i)
        return res