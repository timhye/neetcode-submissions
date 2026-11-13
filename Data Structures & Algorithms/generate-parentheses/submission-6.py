class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rec = defaultdict(int)
        equal = 0
        scrtch = []
        res = []
        

        #i needs to be eqial to n
        # left and right need to be equal

        def dfs(i):
            nonlocal equal
            if i > n * 2 or equal < 0:
                return
            if i == n * 2 and equal == 0:
                res.append("".join(scrtch))
            
            scrtch.append('(')
            equal += 1
            dfs(i + 1)
            scrtch.pop()
            equal -= 1

            scrtch.append(')')
            equal -= 1
            dfs(i + 1)
            scrtch.pop()
            equal += 1

            return
        
        dfs(0)

        return res



