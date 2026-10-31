class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in {'+','-','/','*'}:
                first, second = stk.pop(), stk.pop()
                if token == '+':
                    stk.append(first + second)

                elif token == '*':
                    stk.append(first * second)

                elif token == '/':
                    stk.append(int(second / first))

                elif token == '-':
                    stk.append(second - first)
            else:
                stk.append(int(token))

        return int(stk[0])