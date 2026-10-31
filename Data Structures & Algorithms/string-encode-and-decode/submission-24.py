class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        num = ""
        collect = []
        i = 0
        while i < len(s):
            while s[i] != "#":
                num += s[i]
                i += 1
                
                
            
            cnt = int(num)
            collect.append(s[i+1: i + 1 + cnt])
            num = ""
            i = i + 1 + cnt

        return collect

        

