class Solution:
    def simplifyPath(self, path: str) -> str:
        newstr = path.split('/')
        newstr = [element for element in newstr if element != " "]
        stk = []
        print(newstr)
        for element in newstr:
            if stk and element == '.':
                continue
            
            if stk and element == '..':
                stk.pop()
                continue

            stk.append(element)
        
        itm = '/'.join(stk)
        return '/' + itm


