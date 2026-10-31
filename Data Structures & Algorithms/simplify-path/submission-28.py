class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = path.split("/")
        stk = [value for value in stk if value != ""]
        res = []
        for val in stk:
            if val == "..":
                if res:
                    res.pop()
            elif val == ".":
                continue
            else:
                res.append(val)
            
        return "/" + "/".join(res)