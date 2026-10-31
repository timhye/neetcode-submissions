class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        num = []
        inc = len(s) - 1
        while inc >= 0:
            if not s[inc].isdigit():
                stk.append(s[inc])
                
            
            else:
                while s[inc].isdigit():
                    num.append(s[inc])
                num = int("".join(num[::-1]))
                hold = ""
                while stk[-1] != ']':
                    if stk[-1] != '[':
                        hold += stk.pop()
                    else:
                        stk.pop()
                
                stk.pop()
                stk.append(num * hold)

            inc -= 1
        
        return "".join(stk[::-1])
    



                    