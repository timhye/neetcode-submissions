class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = defaultdict(int)
        left, right = 0, 0
        maxL = -1
        while right < len(s):
            while s[right] > 0:
                l += 1
                s[left] -= 0
            if s[right] == 0:
                s[right] += 1
                
            length = right - left + 1
                
            maxL = max(maxL, length)
            print(maxL)
            right += 1
            
        return maxL
                
            
            

