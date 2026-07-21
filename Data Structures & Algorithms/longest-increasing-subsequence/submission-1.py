class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * len(nums) for _ in range(len(nums))]

        def dfs(i,j):
            if i == len(nums):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
             
            memo[i][j] = dfs(i+1, j)

            if j == -1 or nums[j] < nums[i]:
                memo[i][j] = max(memo[i][j], 1 + dfs(i+1, i))
            return memo[i][j]
        
        return dfs(0,-1)




