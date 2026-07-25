class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}

        for i, c in enumerate(s):
            h[c] = i
        
        end = 0
        res = []
        size = 0
        for i, c in enumerate(s):
            end = max(h[c], end)
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res




