class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        destroy = 0
        for asteroid in asteroids:
            if asteroid < 0:
                while stk:
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
            else:
                stk.append(asteroid)
                print(stk)
        
        return stk
                    
                    
