class Solution:
    def isValid(self, s: str) -> bool:
        record = {"(":")","[":"]","{":"}"}
        stk = []
        for char in s:
            if char in record:
                stk.append(char)
            elif char in record.values():
                if not stk:
                    return False
                if record[stk.pop()] != char:
                    return False
            else:
                continue
        return not stk
                


