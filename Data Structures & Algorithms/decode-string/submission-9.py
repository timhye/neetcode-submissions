class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        num = []
        inc = len(s) - 1
        while inc >= 0:
            if not s[inc].isdigit():
                stk.append(s[inc])
                
            
            else:
                while s[inc].isdigit() and inc >= 0:
                    num.append(s[inc])
                    inc -= 1
                num = int("".join(num[::-1]))
                hold = ""
                while stk[-1] != ']':
                    if stk[-1] != '[':
                        hold += stk.pop()
                    else:
                        stk.pop()
                
                stk.pop()
                stk.append(num * hold)
                num = []

            inc -= 1
        
        return "".join(stk[::-1])
    



                    