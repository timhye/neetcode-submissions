class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left < right:
            total = people[left] + people[right]
            if total > limit:
                right -= 1
                boats += 1
            
            else:
                right -= 1
                left += 1
                boats += 1
            
        
        return boats

