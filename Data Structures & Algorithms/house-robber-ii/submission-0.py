class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[-1] = nums[-1]
        dp2[-2] = max(nums[-1], nums[-2])
        for i in range(2, len(nums)):
            dp1[i] = max(nums[i]+dp1[i-2],dp1[i-1])
        
        for i in range(len(nums)-3, -1, -1):
            print(i)
            dp2[i] = max(nums[i]+dp2[i+2],dp2[i+1])
        
        return max(dp2[1], dp1[-2])
