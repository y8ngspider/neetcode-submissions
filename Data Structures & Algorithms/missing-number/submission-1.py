class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        check = 0
        for i in range(len(nums)+1):
            
            check += i
            print(check)
        return check - total
        
