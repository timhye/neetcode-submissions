class Solution:
    def simplifyPath(self, path: str) -> str:
        newstr = path.split('/')
        newstr = [element for element in newstr if element != ""]
        stk = []
        print(newstr)
        for element in newstr:

            if stk and element == '.':
                continue
            
            if stk and element == '..':
                stk.pop()
                continue
            
            if element != '.' and element != '..':
                stk.append(element)
        
        return "/" + "/".join(stk)


