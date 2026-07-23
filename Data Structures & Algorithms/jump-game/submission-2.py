class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums)-1:
                return True
            
            for n in range(nums[i], 0, -1):
                if dfs(i+n):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)
