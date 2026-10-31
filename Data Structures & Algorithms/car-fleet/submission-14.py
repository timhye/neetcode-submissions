class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        com = []
        for i in range(len(position)):
            com.append((position[i],speed[i]))
        
        com.sort(key=lambda x:x[0])
        print(com)
        fleet = 0
        chk = com.pop()
        time = (target - chk[0]) / chk[1]
        fleet += 1
        while com:
            if (target - com[-1][0]) / com[-1][1] > time:
                fleet += 1
                time = (target - com[-1][0]) / com[-1][1]
            
            com.pop()
        
        return fleet


                

        

        

        