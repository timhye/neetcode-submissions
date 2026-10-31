class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for operation in operations:
            if operation == "C":
                stk.pop()
            
            elif operation[1:].isnumeric():
                stk.append(int(operation))

            elif operation == "+":
                    itm = stk[-1] + stk[-2]
                    stk.append(itm)
            
            elif operation == "D":
                    itm = stk[-1] * 2
                    stk.append(itm)
            
            else:
                stk.append(int(operation))

        return sum(stk)
