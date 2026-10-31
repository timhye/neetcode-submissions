class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for block in path.split("/"):
            if block == '.' or block == '':
                continue
            elif block == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(block)
           
        return "/" + "/".join([block for block in stk if block != ''])


        """by end of this, shld have all things like neetcode, practice, .. and ... etc inside
           looks like ["neetcode","practice","...","..","courses"] inside. Then we rebuild from start,
           as we progress, if we see, "." inside, we can ignore and remove it, if its ".." we need pop
           previous entry and then everything else is we js continue 


        """



            
            
        