class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            itm = str(len(string)) + "#" + string
            res += itm
        return res
    def decode(self, s: str) -> List[str]:
        ori = []
        i, j = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            word = s[j+1:j + 1 + length]

            ori.append(word)

            i = j


                

