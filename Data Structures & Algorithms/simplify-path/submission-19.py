class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = path.split("/")
        print(stk)
        stk = [value for value in stk if value != ""]
        print(stk)