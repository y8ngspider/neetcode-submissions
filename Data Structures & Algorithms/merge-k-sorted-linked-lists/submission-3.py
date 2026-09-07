# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            head = cur = ListNode()
            cur1 = list1
            cur2 = list2
            while cur1 and cur2:
                if cur1.val <= cur2.val:
                    cur.next = cur1
                    cur = cur.next
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur = cur.next
                    cur2 = cur2.next 

            while cur1:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            
            while cur2:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

            return head.next
        
        interval = 1

        while interval < len(lists):
            i = 0

            while i + interval < len(lists):
                lists[i] = merge(lists[i], lists[i + interval])
                i += interval * 2

            interval *= 2

        return lists[0]
