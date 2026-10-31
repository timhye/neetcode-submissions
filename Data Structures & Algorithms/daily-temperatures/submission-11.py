class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = []
        for i in range(len(temperatures)):
            if not stk:
                stk.append((temperatures[i],i))
            else:
                while stk and temperatures[i] > stk[-1][0]:
                    res.append(i - stk[-1][1])
                    stk.pop()

                stk.append((temperatures[i],i))
        return res