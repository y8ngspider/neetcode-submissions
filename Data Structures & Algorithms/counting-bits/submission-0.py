class Solution:
    def countBits(self, n: int) -> List[int]:

        arr = [0] * (n + 1)

        for i in range(n + 1):
            
            x = i
            while x >0:
                if x & 1 == 1:
                    arr[i] += 1
                x = x>>1
        return arr