class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def sol(n,k):
            combs = []
            helper(0, [], combs, 0, nums, target)
            return combs

        def helper(i, curCombs, combs, curSum, nums, k):
            if curSum > k:
                return
            if curSum == k:
                combs.append(curCombs.copy())
                return
            if i >= len(nums):
                return
            

            # include
            curCombs.append(nums[i])
            helper(i, curCombs, combs, curSum + nums[i], nums, k)
            curCombs.pop()
            helper(i+1, curCombs, combs, curSum, nums, k)
        return sol(nums, target)