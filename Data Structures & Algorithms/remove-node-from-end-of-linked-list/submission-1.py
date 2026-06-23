# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length+=1
        
        length = length - n 
        ptr = head
        if length==0:
            head = head.next
        else:
            for i in range(length-1):
                ptr = ptr.next
            prev = ptr
            ptr = ptr.next.next
            prev.next = ptr
        return head