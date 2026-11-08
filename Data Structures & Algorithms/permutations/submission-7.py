class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        scratch = []
        avail = list(nums)
        def dfs(i, chosen):
            
            
            avail.remove(chosen)
            scratch.append(chosen)

            if not avail:
                res.append(list(scratch))
            
            check = list(avail)
            if i < len(nums):
                for num in check:
                    dfs(i + 1, num)
                
            avail.append(chosen)
            scratch.pop()

            

            

        for num in nums:
            dfs(0, num)
        
        return res
            
            

            
