class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        rec = Counter(s1)
        left = 0

        for right in range(len(s2)):
            rec[s2[right]] -= 1

            if right - left + 1 > len(s1):
                rec[s2[left]] += 1
                left += 1

            if right - left + 1 == len(s1) and all(freq == 0 for freq in rec.values()):
                return True

        return False