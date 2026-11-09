class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        scratch = []
        rec = {}
        rec['2'] = ['a', 'b', 'c']
        rec['3'] = ['d', 'e', 'f']
        rec['4'] = ['g', 'h', 'i']
        rec['5'] = ['j', 'k', 'l']
        rec['6'] = ['m', 'n', 'o']
        rec['7'] = ['p', 'q', 'r', 's']
        rec['8'] = ['t', 'u', 'v']
        rec['9'] = ['w','x', 'y', 'z']

        if not digits:
            return []
        def dfs(i):
            if i == len(digits):
                res.append("".join(scratch))
                return
            
            if i < len(digits):
                for num in rec[digits[i]]:
                    scratch.append(num)
                    dfs(i + 1)
                    scratch.pop()

        dfs(0)

        return res

        
