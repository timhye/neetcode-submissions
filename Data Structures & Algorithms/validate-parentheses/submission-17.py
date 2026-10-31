class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        record = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stk.append(char)
                continue
            
            else:
                if stk and stk.pop() != record[char]:
                    return False
        
        if stk:
            return False

        return True

            
