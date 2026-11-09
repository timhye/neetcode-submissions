class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rec = defaultdict(list)
        res = []
        for string in strs:
            id = [0] * 26
            for char in string:
                id[ord(char) - 97] += 1

            rec[tuple(id)].append(string)

        for vals in rec.values():
            res.append(vals)

        return res 
