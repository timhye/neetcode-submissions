class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """For this the combinations of 2 asteroids interacting is + + , + -
            , - + and -- for which only the second case has the chance 
            for collision"""

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                continue
            else:
                check = i - 1
                while check >= 0 and asteroids[check] > 0:
                    if asteroids[check] == 0:
                        check -= 1
                        continue
                    if asteroids[check] > -asteroids[i]:
                        asteroids[i] = 0
                        break
                    elif asteroids[check] == -asteroids[i]:
                        asteroids[i] = 0
                        asteroids[check] = 0
                        break
                    else:
                        asteroids[check] = 0
                        check -= 1
        

        asteroids = [x for x in asteroids if x != 0]
        return asteroids

