class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            itm = str(len(string)) + "#" + string
            res += itm
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        ori = []
        itm = ""
        num = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
                continue
            ite = int(num)
            while ite > 0:
                itm += s[i + 1]
                i += 1
                ite -= 1
            
            ori.append(itm)
            print("itm" + itm, "num" + num)
            num = ""
            itm = ""
        return ori


                

