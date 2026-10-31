class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        can1, can2 = 0, 0
        cnt1, cnt2 = 0, 0 
        for num in nums:
            if num == can1:
                cnt1 += 1
            elif num == can2:
                cnt2 += 1
            elif cnt1 == 0:
                can1 = num
                cnt1 += 1
            elif cnt2 == 0:
                can2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        


        return [x for x in [can1,can2] if x != 0]


