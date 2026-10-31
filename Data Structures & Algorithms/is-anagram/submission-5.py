class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fors = {}
        fort = {}
        if len(s) != len(t):
            return False
        for char in s:
            fors[char] = fors.get(char,0) + 1
        
        for char in t:
            fort[char] = fort.get(char,0) + 1
        
        for key,value in fors.items():
            if key in fort and (key,value) == (key,fort[key]):
                continue
            else:
                return False

        return True