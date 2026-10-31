class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + '#' + string)

        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num = ""
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
            else:
                res.append(s[i+1 : i + 1 + int(num)])
                i += (int(num) + 1)
                num = ""

        return res
        

