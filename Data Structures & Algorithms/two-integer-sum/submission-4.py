class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            hm[n] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm and hm[diff] != i:
                return [i,hm[diff]]