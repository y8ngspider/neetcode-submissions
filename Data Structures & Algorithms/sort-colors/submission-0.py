class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        res = []
        for i in range(len(nums)):
            freq[nums[i]]+=1
        x=0
        for j in range(len(freq)):
            for y in range(freq[j]):
                nums[x] = j
                x+=1

        