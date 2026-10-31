class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        inc = len(s) - 1
        while inc >= 0:
            if not s[inc].isdigit():
                stk.append(s[inc])
                
            
            else:
                num = int(s[inc])
                hold = ""
                while stk[-1] != ']':
                    if stk[-1] != '[':
                        hold += stk.pop()
                    else:
                        stk.pop()
                
                stk.pop()
                stk.append(num * hold)

            inc -= 1
        
        return "".join(stk)
    



                    