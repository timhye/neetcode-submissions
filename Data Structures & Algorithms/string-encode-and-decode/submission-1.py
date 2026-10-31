class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            length = str(len(s))
            length += ('#' + s)
            encoded += length

        return encoded
            

    def decode(self, s: str) -> List[str]:
        newlist = []
        length = 0
        i = 0
        while s[i] < len(s) - 1:
            if 48 <=ord(s[i]) <= 57:
                length += s[i]
                i += 1
                continue
            
            num = int(length)
            if s[i] == '#':
                string = ""
                for add in range(1,num + 1):
                    string += s[i + add]
                
                newlist.append(string)
                length = 0

                i = i + num + 2
            
        return newlist
                


            




            

