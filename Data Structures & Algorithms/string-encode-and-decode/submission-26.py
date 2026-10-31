class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for each in strs:
            res += (str(len(each)) + '#' + each)
        print(res)


    def decode(self, s: str) -> List[str]:
        pass
