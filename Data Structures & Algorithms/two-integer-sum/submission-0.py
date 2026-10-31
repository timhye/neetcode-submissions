class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = sorted(nums)
        data = {}

        for i in range(len(nums)):
            data[nums[i]] = i 
        
        print(data)

        i, j = 0, len(nums) - 1
        print(i,j)
        while i < j:
            total = check[i] + check[j]
            if total == target:
                lower, higher = check[i], check[j]
                break
            elif total < target:
                i += 1
                pass
            elif total > target:
                j -= 1
                pass
        print(lower, higher)

        answer = [data[lower], data[higher]]
        
        return answer
                            