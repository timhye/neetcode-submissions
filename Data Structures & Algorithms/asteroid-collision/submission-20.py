class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        stk.append(asteroids[0])
        alive = 0
        for asteroid in asteroids:
            if len(stk) == 0:
                stk.append(asteroid)
                continue
            alive = 1
            while stk[-1] > 0 and asteroid < 0:
                if stk[-1] < abs(asteroid):
                    stk.pop()
                elif stk[-1] > abs(asteroid):
                    alive = 0
                    break
                else:
                    stk.pop()
                    alive = 0
                    break

            if alive:
                stk.append(asteroid)

        return stk
        
        