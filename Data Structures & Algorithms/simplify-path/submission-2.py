class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        snip = ""
        for i in range(len(path)):
            if path[i] == '/' and len(snip) == 0:
                continue
            elif path[i] == '/' and len(snip) != 0:
                stk.append(snip)
                snip = ""
                continue
            else:
                snip += path[i]
        
        if len(snip) != 0:
            stk.append(snip)
        print(stk)
        for j in range(len(stk)):
            if stk[j] == '.':
                stk[j] = ''
            elif stk[j] == '..':
                stk[j - 1] = ''
                stk[j] = ''
            else:
                continue
        
        stk = [block for block in stk if block != '']
        print(stk)
        return "/" + "/".join(stk)


        """by end of this, shld have all things like neetcode, practice, .. and ... etc inside
           looks like ["neetcode","practice","...","..","courses"] inside. Then we rebuild from start,
           as we progress, if we see, "." inside, we can ignore and remove it, if its ".." we need pop
           previous entry and then everything else is we js continue 


        """



            
            
        