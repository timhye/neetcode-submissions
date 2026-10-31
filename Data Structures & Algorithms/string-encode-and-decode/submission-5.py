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
        length = ""
        i = 0
        while i < len(s):
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
                length = ""


                i = i + num + 1
            
        return newlist
                


            




            

