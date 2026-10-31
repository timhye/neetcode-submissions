class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = 0
        pre = ""
        while first < min(len(strs[0]), len(strs[len(strs)-1])):
            if strs[0][first] == strs[len(strs)-1][first]:
                pre += strs[0][first]
                first += 1
        
            else:
                return pre
            
        
        return pre
