class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for each in strs:
            res += (str(len(each)) + '#' + each)
        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        num = ""
        char = 0
        while char < len(s):
            if s[char].isdigit():
                num += s[char]
                char += 1
            
            else:
                res.append(s[char + 1: char + 1 + int(num)])
                char = char + 1 + int(num)
                print(char)
        
        return res

            
            
                






        
