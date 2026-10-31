class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        hm1 = defaultdict(int)
        for i in range(len(s1)):
            hm1[s1[i]] += 1
        
        hm2 = defaultdict(int)
        for right in range(len(s2)):
            hm2[s2[right]] += 1
            if (right - left + 1) == len(s1) and hm1 == hm2:
                return True
            
            else:
                hm2[s2[left]] -= 1
                left += 1
        
        return False




