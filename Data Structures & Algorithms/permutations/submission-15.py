class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        scratch = []
        res = []
        used = [False] * len(nums)
        def dfs():
            if all(used):
                res.append(list(scratch))
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    scratch.append(nums[i])
                    dfs()
                    used[i] = False
                    scratch.pop()

        dfs()

        return res
        
        
