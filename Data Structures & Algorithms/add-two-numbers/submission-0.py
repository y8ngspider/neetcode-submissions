# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Start from last digit
        # Define Cases:
        # 1. Digit is < 10, just add both digits tgt, continue
        # 2. Digit > 10, keep the carry, add to next digit
        # 3. Need to add new node, same as case 2

        # Create dummy node
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        # Iterate through list, adding both val of both list tgt then create new node
        while l1 or l2 or carry:
            if l1 and l2 == None:
                val = l1.val + carry
                l1 = l1.next
            elif l2 and l1 == None:
                val = l2.val + carry
                l2 = l2.next
            elif l2 and l1:
                val = l2.val + l1.val + carry
                l1 = l1.next
                l2 = l2.next
            else:
                val = carry
            cur.next = ListNode(val) if val < 10 else ListNode(val%10)
            cur = cur.next
            carry = 0 if val < 10 else val//10
            
        return dummy.next            
            





