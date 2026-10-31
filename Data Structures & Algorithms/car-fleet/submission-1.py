class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos,spd) for pos,spd in zip(position,speed)]
        print(cars)