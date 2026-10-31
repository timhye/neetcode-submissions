class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            destroy = 0

        
            while stk and asteroid < 0 and stk[-1] > 0:
                check = stk[-1]
                if check > abs(asteroid):
                    destroy = 1
                    
                
                elif check == abs(asteroid):
                    stk.pop()
                    destroy = 1
                
                else:
                    stk.pop()
                
            if not destroy:
                stk.append(asteroid)
                break
           
        
        return stk
                    
                    
