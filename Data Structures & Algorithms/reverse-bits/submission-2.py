class Solution:
    def reverseBits(self, n: int) -> int:
       
        res=0
        ans = ''
        for i in range(32):
            res = res << 1
            if n & 1 == 1:
                ans += '1'
                res = res | 1         
            n = n >> 1

        return res