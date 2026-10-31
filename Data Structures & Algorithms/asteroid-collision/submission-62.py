class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """For this the combinations of 2 asteroids interacting is + + , + -
            , - + and -- for which only the second case has the chance 
            for collision"""

        stk = []
        for asteroid in asteroids:
            destroy =False
            
            while stk and stk[-1] > 0 and asteroid < 0:
                if stk[-1] < 0:
                    break
                if stk[-1] > abs(asteroid):
                    destroy = True
                    break
                elif stk[-1] == abs(asteroid):
                    stk.pop()
                    destroy = True
                    break
                else:
                    stk.pop()
            
            if not destroy:
                stk.append(asteroid)

        return stk
                
