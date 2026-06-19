# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        i = 0
        start = head
        arr = []
        while start:
            arr.append(start.val) 
            start = start.next
        
        maxSum = 0
        for i in range(len(arr)//2):
            twinSum = arr[i]+arr[len(arr)-1-i]
            maxSum = max(maxSum, twinSum)
        
        return maxSum