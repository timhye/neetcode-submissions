class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """For this the combinations of 2 asteroids interacting is + + , + -
            , - + and -- for which only the second case has the chance 
            for collision"""

        stk = []
        for asteroid in asteroids:
            destroy = 0
            
            while stk and stk[-1] > 0 and asteroid < 0:
                if stk[-1] < 0:
                    break
                if stk[-1] > abs(asteroid):
                    destroy = 1
                    break
                elif stk[-1] == abs(asteroid):
                    stk.pop()
                    destroy = 1
                    break
                else:
                    stk.pop()
            
            if destroy == 0:
                stk.append(asteroid)

        return stk
                
