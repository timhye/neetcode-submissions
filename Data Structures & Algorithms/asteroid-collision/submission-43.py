class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for asteroid in asteroids:
            destroy = False

            while stk and asteroid < 0 and stk[-1] > 0:
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