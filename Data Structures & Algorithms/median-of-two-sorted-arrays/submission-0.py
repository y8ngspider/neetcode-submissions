class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2

        #make sure A is always the shorter one
        if len(B) < len(A):
            A, B = B, A
        
        l = 0 
        r = len(A) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2

            aleft = A[i] if i >=0 else -float('inf')
            aright = A[i+1] if i+1<len(A) else float('inf')
            bleft = B[j] if j>=0 else -float('inf')
            bright = B[j+1]  if j+1<len(B) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright,bright)
                else:    
                    return (max(aleft,bleft) + min(aright,bright))/2

            else:
                if aleft > bright:
                    r = i - 1
                else:
                    l = i + 1
            
