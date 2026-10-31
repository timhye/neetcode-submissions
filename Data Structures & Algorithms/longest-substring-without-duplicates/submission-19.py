class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)
        left, right = 0, 0
        maxL = -1
        while right < len(s):
            store[right] += 1
            while store[right] > 1:
                store[left] -= 0
                l += 1

            length = right - left + 1
                
            maxL = max(maxL, length)
            right += 1
            
        return maxL
                
            
            

