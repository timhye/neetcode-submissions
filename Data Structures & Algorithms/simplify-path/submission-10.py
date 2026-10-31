class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        clean = path.split('/')
        for block in clean:
            if block == '.' or not block:
                continue
            elif block == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(block)
           
        return "/" + "/".join(stk)


        """by end of this, shld have all things like neetcode, practice, .. and ... etc inside
           looks like ["neetcode","practice","...","..","courses"] inside. Then we rebuild from start,
           as we progress, if we see, "." inside, we can ignore and remove it, if its ".." we need pop
           previous entry and then everything else is we js continue 


        """



            
            
        