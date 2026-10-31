class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        cnt = 0
        rec = set()
        for char in s:
            if char not in rec:
                print(char)
                cnt += 1
                rec.add(char)
                continue
            
            longest = max(longest, cnt)
            cnt = 0
            rec.clear()

        return longest

