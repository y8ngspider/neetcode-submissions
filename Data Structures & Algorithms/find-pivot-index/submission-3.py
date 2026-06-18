class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        postfix = [0] * len(nums)
        pre, post = 0, 0
        for n in nums:
            pre += n
            prefix.append(pre)
        for i in range(len(nums)-1, -1, -1):
            post += nums[i]
            postfix[i] = post 
        
        for i in range(len(nums)):
            left_sum = prefix[i-1] if i > 0 else 0
            right_sum = postfix[i+1] if i < len(nums) - 1 else 0
            if left_sum == right_sum:
                return i
        
        return -1