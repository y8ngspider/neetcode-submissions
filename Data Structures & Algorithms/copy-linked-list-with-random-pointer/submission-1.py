"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        arr = {}
        if cur == None:
            return head


        newHead = Node(cur.val)
        newCur = newHead
        while cur and cur.next:
            arr[cur] = newCur
            newCur.next = Node(cur.next.val)
            cur = cur.next
            newCur = newCur.next
        arr[cur] = newCur

        for key, val in arr.items():
            if key.random != None:
                val.random = arr[key.random]
        
        return newHead


        