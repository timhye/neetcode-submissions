class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        total = 0
        for operation in operations:
            if operation.isnumeric():
                stk.append(int(operation))

            elif operation == "+":
                itm = stk[-1] + stk[-2]
                stk.append(itm)
                total += itm
            
            elif operation == "D":
                if stk:
                    itm = stk[-1] * 2
                    stk.append(itm)
            
            else:
                stk.pop()
                

        
        return sum(stk)
