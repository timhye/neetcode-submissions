class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ops in operations:
            if isinstance(ops, int):
                stk.append(ops)
                continue
            elif ops == '+':
                stk.append(stk[-1] + stk[-2])
            elif ops == 'D':
                stk.append(2 * stk[-1])
            else:
                stk.pop()
        
        return sum(stk)