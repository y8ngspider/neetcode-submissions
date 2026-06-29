class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def sol(n,k):
            candidates.sort()
            combs = []
            helper(0, [], combs, 0, candidates, target)
            return combs


        def helper(i, curCombs, combs, curSum, candidates, k):
            if curSum > k:
                return
            if curSum == k:
                combs.append(curCombs.copy())
                return
            if i >= len(candidates):
                return
            
            curCombs.append(candidates[i])
            helper(i+1, curCombs, combs, curSum + candidates[i], candidates, k)
            curCombs.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i+1, curCombs, combs, curSum, candidates, k)


        return sol(candidates, target)