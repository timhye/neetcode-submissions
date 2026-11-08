class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        scratch = []
        avail = list(nums)
        def dfs(chosen):
            
            
            avail.remove(chosen)
            scratch.append(chosen)

            if not avail:
                res.append(list(scratch))
            
            check = list(avail)
            
            for num in check:
                dfs(num)
                
            avail.append(chosen)
            scratch.pop()

            

            

        for num in nums:
            dfs(num)
        
        return res
            
            

            
