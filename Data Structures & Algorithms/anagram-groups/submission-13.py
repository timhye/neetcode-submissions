class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        store = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - 97] += 1
            
            store[tuple(arr)].append(string)
        
        for v in store.values():
            if len(v) > 0:
                res.append(v)
            
        return res
                
        

            

            


