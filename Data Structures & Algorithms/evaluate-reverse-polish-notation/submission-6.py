class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        if tokens is None:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token not in {'+','/','-','*'}:
                stk.append(token)
            
            else:
                a = int(stk.pop())
                b = int(stk.pop())
                match token:
                    case '+': 
                        stk.append(a + b)
                    
                    case '-':
                        stk.append(b - a)
                    
                    case '*':
                        stk.append(a*b)
                    
                    case '/':
                        stk.append(b/a)

        final = int(stk.pop())
        
        return final
                        