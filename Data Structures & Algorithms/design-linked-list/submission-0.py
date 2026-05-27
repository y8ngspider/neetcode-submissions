class Node:
    def __init__(self, val: int, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.head ==None or index>self.length-1:
            return -1
        else:
            pointer = self.head
            for i in range(index):
                pointer = pointer.next
            return pointer.val


    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            new = Node(val)
            self.head = new
            self.tail = new
            self.length=self.length+1
            return
        new = Node(val)
        temp = self.head
        new.next = temp
        temp.prev = new
        self.head = new
        self.length=self.length+1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            new = Node(val)
            self.head = new
            self.tail = new
            self.length=self.length+1
            return
        new = Node(val)
        temp = self.tail
        temp.next = new
        new.prev = temp
        self.tail = new
        self.length=self.length+1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return
        elif index <= 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
        else:
            pointer = self.head
            new = Node(val)
            for i in range(index):
                pointer = pointer.next
            prev = pointer.prev
            new.next = pointer
            new.prev = prev
            prev.next = new
            pointer.prev = new
            self.length=self.length+1
        

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.length or index<0:
            return
        if self.length==1:
                self.head = None
                self.tail = None
        elif index ==0:
            self.head = self.head.next
            self.head.prev = None
            
        elif index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            pointer = self.head
            for i in range(index):
                pointer = pointer.next
            next = pointer.next
            prev = pointer.prev
            next.prev = prev
            prev.next = next
        self.length=self.length-1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)