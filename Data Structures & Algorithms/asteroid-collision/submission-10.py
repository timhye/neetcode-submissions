class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        stk.append(asteroids[0])
        for i in range(1,len(asteroids)):
            if len(stk) != 0:
                cur = stk[-1]
                if cur > 0:
                    if asteroids[i] < 0:
                        if cur == -asteroids[i]:
                            stk.pop()
                            continue
                        if max(cur, abs(asteroids[i])) == cur:
                            continue
                        else:
                            stk.pop()
                            while stk is not None:
                                if stk[-1] > 0:
                                    if max(stk[-1], abs(asteroids[i])) == stk[-1]:
                                        break
                                    else:
                                        stk.pop()
                                        continue

                    
                    else:
                        stk.append(asteroids[i])
                        continue

                
                else:
                    stk.append(asteroids[i])

            else:
                stk.append(asteroids[i])
            
        
        return stk
        