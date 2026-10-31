class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        total = 0
        for operation in operations:
            if operation.isnumeric():
                stk.append(int(operation))

            elif operation == "+":
                if stk and len(stk) > 1:
                    itm = stk[-1] + stk[-2]
                    stk.append(itm)
                    total += itm
            
            elif operation == "D":
                if stk:
                    itm = stk[-1] * 2
                    stk.append(itm)
                    print(stk)
            
            else:
                if stk:
                    stk.pop()
                

        
        print(stk)
        return sum(stk)
