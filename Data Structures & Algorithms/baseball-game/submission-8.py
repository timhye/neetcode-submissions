class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ops in operations:
            if ops.isnumeric() or ops[1:].isnumeric():
                stk.append(int(ops))
                continue
            elif ops == '+':
                stk.append(stk[-1] + stk[-2])
            elif ops == 'D' and len(stk) != 0:
                stk.append(2 * stk[-1])
            else:
                    stk.pop()
        
        total = 0
        for score in stk:
            total += score

        return score