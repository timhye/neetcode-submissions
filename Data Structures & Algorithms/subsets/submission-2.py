class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
            # [1,2,3]
        def dfs(i, current):
            if i == len(nums):
                res.append(list(current))
                return 
            
            current.append(nums[i])
            dfs(i + 1, current)
            current.pop()
            dfs(i + 1, current)

            return
        
        dfs(0, [])

        return res


        
