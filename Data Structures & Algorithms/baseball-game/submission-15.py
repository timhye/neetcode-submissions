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
                print(stk)
                itm = 2 * stk[-1]
                stk.append(itm)
            
            else:
                stk.pop()
                continue

        
        return total
