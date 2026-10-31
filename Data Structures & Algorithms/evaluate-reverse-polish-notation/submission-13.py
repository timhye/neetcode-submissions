class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in {'+','-','/','*'}:
                first, second = int(stk.pop()), int(stk.pop())
                if token == '+':
                    stk.append(first + second)

                elif token == '*':
                    stk.append(first * second)

                elif token == '/':
                    stk.append(second / first)

                elif token == '-':
                    stk.append(second - first)
            else:
                stk.append(token)

        
        return stk[0]