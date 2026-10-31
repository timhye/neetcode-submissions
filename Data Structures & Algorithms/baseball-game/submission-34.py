class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        total = 0
        for operation in operations:
            if operation == "C":
                total -= stk.pop()

            elif operation == "+":
                    itm = stk[-1] + stk[-2]
                    stk.append(itm)
                    total += itm
            
            elif operation == "D":
                    itm = stk[-1] * 2
                    stk.append(itm)
                    total += itm
            
            else:
                stk.append(int(operation))
                total += int(operation)

        return total
