class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
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
                        stk.append(a - b)
                    
                    case '*':
                        stk.append(a*b)
                    
                    case '/':
                        stk.append(a/b)
        
        return stk.pop()
                        