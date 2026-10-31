class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        stack = []
        pair = {")": "(", "]":"[","}":"{"}
        
        for c in s:
            if c in pair.keys():
                if stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True
        