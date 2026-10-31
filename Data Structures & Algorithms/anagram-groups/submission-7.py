class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                num = ord(c) - ord('a')
                count[num] += 1
            groups[str(count)].append(s)
            

        return list(groups)