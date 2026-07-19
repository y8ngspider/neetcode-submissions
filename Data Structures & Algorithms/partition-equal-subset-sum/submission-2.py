class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        arrSum = 0
        for num in nums:
            arrSum += num

        if arrSum % 2 != 0:
            return False

        def dfs(i, target, total):
            if i == len(nums):
                if total == target:
                    return True
                return False
            
            if (i, total) in memo:
                return memo[i,total]
            
            memo[i,total] = dfs(i+1, target, total) or dfs(i+1, target, total + nums[i])
            return memo[i, total]

        return dfs(0, arrSum//2, 0)