class Solution:
    def reverse(self, x: int) -> int:
        NEGATIVE = ~(0x7FFFFFFF - 1)
        POSITIVE = 0x7FFFFFFF
        
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
        
            if res > POSITIVE // 10 or (res == POSITIVE//10 and digit > POSITIVE % 10):
                return 0
            elif res < NEGATIVE // 10 or (res == NEGATIVE//10 and digit < NEGATIVE % 10):
                return 0
            res = (res*10)+digit
        return res