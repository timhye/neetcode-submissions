class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        stk.append(asteroids[0])
        for i in range(1,len(asteroids)):
            cur = stk[-1]
            if cur > 0:
                if asteroids[i] < 0:
                    if max(cur, abs(asteroids[i])) == cur:
                        continue
                    else:
                        stk.pop()
                        stk.append(asteroids[i])
                
                else:
                    continue

            
        
        return stk
        