class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            # Base - if m is the target, return
            if nums[m] == target:
                return m
            
            # Split into 2 cases, then subcases.
            # left is smaller than mid, so we're in left sorted portion
            if nums[l] <= nums[m]:
                
                # Basically means that target is not in the left sorted
                if target > nums[m] or target < nums[l]:
                    # Target, is in right half, move to right
                    l = m + 1
                # Else, target is in left half, search here
                else:
                    r = m -1 
            
            # Else, target is in right portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1