class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for i in range(len(asteroids)):
            survive = True
            if asteroids[i] < 0:
                while stk:
                    
                    if stk[-1] == abs(asteroids[i]):
                        stk.pop()
                        survive = False
                        break
                    
                    if stk[-1] > abs(asteroids[i]):
                        survive = False
                        break
                    
                    
                    
                    if stk[-1] < abs(asteroids[i]):
                        stk.pop()
                        continue
                
                
            if survive:
                stk.append(asteroids[i])
        
        return stk
