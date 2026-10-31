class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            destroy = False

        
            while stk and asteroid < 0 and stk[-1] > 0:
                check = stk[-1]
                if check > abs(asteroid):
                    destroy = True
                    break
                    
                
                elif check == abs(asteroid):
                    stk.pop()
                    destroy = True
                    break

                
                else:
                    stk.pop()
                
            if not destroy:
                stk.append(asteroid)
                
           
        
        return stk
                    
                    
