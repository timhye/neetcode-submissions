class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers) - 1
        while left < right:
            sum = numbers[left - 1] + numbers[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
                continue
            else:
                right -= 1
                continue
        
        return [left, right]