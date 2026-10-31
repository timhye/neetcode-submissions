class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token != "+" and token != "*" and token != "-" and token != "/":
                stk.append(token)
            else:
                a = int(stk.pop())
                b = int(stk.pop())
                if token == "+":
                    stk.append(a + b)
                
                elif token == "*":
                    stk.append(a * b)

                elif token == "/":
                    stk.append(b / a)
                
                else:
                    stk.append(b - a)
        
        return stk[0]

        