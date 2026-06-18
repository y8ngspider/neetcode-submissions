class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # must eat in h hours
        # want to find rate of bananas k 
        # if >k bananas, finish eating
        # upperbound is h, lower bound is no. of piles
        # worst case(upper bound) is h
        l = 1
        r = max(piles)
        num = 0

        while l<=r:
            m = math.floor((l+r)/2)
            test = 0
            for n in piles:
                test += math.ceil(n/m)
            if test>h:
                l = m+1
            elif test<=h:
                r = m-1
        return l

        

