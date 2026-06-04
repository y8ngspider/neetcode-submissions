class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #pile
        #banana in pile
        #h hours
        #k - minimum banana per hour        
        # sum(piles) = # of piles * piles[i]
        # k*h >= sum(piles)
        # h >= # of piles
        n=0 
        right=-1
        for i in range(len(piles)):
            n += piles[i]
            if piles[i] > right:
                right = piles[i]

        l=1
        r=right
        k=right
        while l<=r:
            x=0
            m=(l+r)//2
            if m == 0: break
            for i in range(len(piles)):
                x+= (piles[i] + m - 1) // m
            if x>h:
                l=m+1
            else:
                k=m
                r=m-1
        return k
