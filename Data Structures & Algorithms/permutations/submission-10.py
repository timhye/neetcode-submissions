class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        scratch = []
        used = [False] * len(nums)
        def dfs(i):
            
            used[i] = True
            scratch.append(nums[i])

            if all(used):
                res.append(list(scratch))
            
            for j in range(len(nums)):
                if not used[j]:
                    dfs(j)
                
            used[i] = False
            scratch.pop()

            

            

        for i in range(len(nums)):
            dfs(i)
        
        return res
            
            

            
