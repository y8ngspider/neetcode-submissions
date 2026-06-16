class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax, 0) + n
            curMin = min(curMin+n,n)
            minSum = min(curMin, minSum)
            maxSum = max(curMax, maxSum)
            total += n
        if total == minSum:
            return maxSum
        return max(total-minSum, maxSum)






