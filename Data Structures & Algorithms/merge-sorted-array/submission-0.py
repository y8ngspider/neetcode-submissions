class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif n==0:
            return
        x = m + n - 1
        l = m-1
        r = n-1
        while l>=0 and r>=0:
            if nums1[l] < nums2[r]:
                nums1[x] = nums2[r]
                r -=1
                x -= 1
            elif nums1[l] >= nums2[r]:
                nums1[x] = nums1[l]
                l -= 1
                x -= 1
        if r>=0:
            for i in range(r+1):
                nums1[i] = nums2[i]