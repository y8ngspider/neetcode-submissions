class Solution:
    def reverse(self, x: int) -> int:
        negative = ~(0x7FFFFFFF - 1)
        positive = 0x7FFFFFFF
        
        x = str(x)
        res = ''
        if x[0] == '-':
            res += '-'
            x = x[1:]
        
        for i in range(len(x)-1, -1, -1):
            res += x[i]
        res= int(res)
        return res if res < positive and res > negative else 0

