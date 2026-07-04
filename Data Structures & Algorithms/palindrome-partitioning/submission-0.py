class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # palindrome req - same one way and the other way
        # backtracking
        combs=[]
        def dfs(i, s, curComb, combs):
            if i == len(s):
                combs.append(curComb.copy())

            for j in range(i+1,len(s)+1):
                if isValid(s[i:j]):
                    curComb.append(s[i:j])
                    dfs(j,s,curComb,combs)
                    curComb.pop()            
        
        def isValid(check):
            i = 0
            j = len(check)-1
            while i < j:
                if check[i] !=check[j]:
                    return False
                i +=1
                j -=1
            return True
        
        dfs(0,s,[],combs)
        return combs