class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = []
        subset_without_first = self.subsets(nums[1:])
        for s in subset_without_first:
            res.append([nums[0]] + s)
        return res + subset_without_first