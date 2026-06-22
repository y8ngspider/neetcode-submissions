# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        l = []
        curr = head
        while curr != None:
            l.append(curr)
            curr=curr.next

        R=len(l)-1
        for L in range(int(len(l)/2)):
            l[L].next = l[R]
            l[R].next = l[L+1]
            R-=1
        
        l[len(l)//2].next = None