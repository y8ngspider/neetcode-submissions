class Node:
    def __init__(self, val: str, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        new = Node(url)
        self.cur.next = new
        new.prev = self.cur
        self.cur = new       

    def back(self, steps: int) -> str:
        for i in range(steps):
            if(self.cur.prev != None):
                self.cur = self.cur.prev
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if(self.cur.next != None):
                self.cur = self.cur.next
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)