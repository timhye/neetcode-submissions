class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for i in range(len(asteroids)):
            survive = 1
            if asteroids[i] < 0:
                while stk:
                    if stk[-1] > asteroids[i]:
                        survive = 0
                        break
                    
                    if stk[-1] == abs(asteroids[i]):
                        stk.pop()
                        survive = 0
                        break
                    
                    if stk[-1] < asteroids[i]:
                        stk.pop()
                        continue
                
                
            if survive:
                stk.append(asteroids[i])
        
        return stk
