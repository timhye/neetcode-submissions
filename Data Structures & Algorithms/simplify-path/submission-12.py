class Solution:
    def simplifyPath(self, path: str) -> str:
        newstr = path.split('/')
        stk = []
        for element in newstr:
            if stk and element == '.':
                continue
            
            if stk and element == '..':
                stk.pop()
                continue

            stk.append(element)
        
        return '/' + ('/'.join(stk))


