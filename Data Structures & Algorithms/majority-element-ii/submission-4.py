class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, cnt1, cnt2 = 0,0,0,0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
            elif cnt2 == 0:
                num2 = num
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        
        res = []
        if num1 != 0:
            res.append(num1)
        if num2 != 0:
            res.append(num2)
        return res