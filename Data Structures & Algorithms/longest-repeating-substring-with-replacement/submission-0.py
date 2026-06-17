class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #i think just find longest subarray + k?

        L = 0
        length = 0
        window = {}
        for R in range(len(s)):
            if s[R] not in window:
                window[s[R]] = 1
            else:
                window[s[R]] +=1
            while (R-L+1) - max(window.values()) > k:
                window[s[L]]-=1
                L+=1
            length = max(length, R-L+1)            
        return length 
        
