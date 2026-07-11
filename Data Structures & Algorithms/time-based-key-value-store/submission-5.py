class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if key in self.timemap:
            arr = self.timemap[key]
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l+r)//2
                if arr[m][0] > timestamp:
                    r = m-1
                elif arr[m][0] <= timestamp:
                    l = m+1
                    res=arr[m][1]
        return res
        
