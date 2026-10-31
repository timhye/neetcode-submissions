class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        prefix = ''
        while i < len(first) and i < len(last) and first[i] == last[i]:
            prefix += first[i]
            i += 1
        
        return prefix
