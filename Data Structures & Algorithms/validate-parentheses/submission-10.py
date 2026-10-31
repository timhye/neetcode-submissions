class Solution:
    def isValid(self, s: str) -> bool:
        record = {"(":")","[":"]","{":"}"}
        stk = []
        for char in s:
            if char in record:
                stk.append(char)
            elif char in record.values():
                if len(stk) != 0 and record[stk.pop()] != char:
                    return False
            else:
                continue
        if len(stk) != 0:
            return False
        return True
                


