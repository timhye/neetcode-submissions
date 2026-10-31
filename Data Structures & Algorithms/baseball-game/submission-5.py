class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ops in operations:
            if ops.isnumeric():
                stk.append(int(ops))
                print(stk)
                continue
            elif ops == '+':
                stk.append(int(stk[-1] + stk[-2]))
            elif ops == 'D' and len(stk) != 0:
                stk.append(2 * int(stk[-1]))
            else:
                if len(stk) != 0:
                    stk.pop()
        
        return sum(stk)