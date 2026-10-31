class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            itm = str(len(string)) + "#" + string
            res += itm
        return res
    def decode(self, s: str) -> List[str]:
        ori = []
        num = ""
        itm = ""
        for i in range(len(s)):
            if s[i] != "#":
                num += s[i]
                continue
            ite = int(num)
            while ite > 0:
                itm += s[i + 1]
                i += 1
                ite -= 1
        
            ori.append(itm)
        
        return ori


                

