class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt = 0
        l, r = 0, len(people) - 1
        while l < r:
            if people[r] == limit:
                cnt += 1
                continue
            elif people[l] + people[r] <= limit:
                cnt += 1
            else:
                cnt += 2
        
        return cnt
