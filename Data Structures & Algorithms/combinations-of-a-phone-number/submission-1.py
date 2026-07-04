class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {"2":"abc","3":"def","4":"ghi","5":"jkl",
        "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}

        res = []
        if len(digits) == 0:
            return res
        def backtrack(i, curStr):
            if len(curStr)==len(digits):
                res.append(curStr)
                return
            # for each character per number
            for char in table[digits[i]]:
                # go to next 
                backtrack(i+1, curStr+char)


        backtrack(0, "")
        return res

