class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt = 0
        l, r = 0, len(people) - 1
        while l < r:
            total = people[r] + people[l]
            if total <= limit:
                cnt += 1
                l += 1
            else:
                cnt +=1 
            
            r -= 1
        
        if l == r:
            return cnt + 1

        
        return cnt
