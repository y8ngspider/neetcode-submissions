class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt = {}
        window = {}
        
        for c in t:
            freqt[c] = freqt.get(c,0) + 1
        
        L = 0
        have, need = 0, len(freqt)
        res = (0,0)
        length = float('inf')

        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c,0) + 1
            
            if c in freqt and freqt[c] == window[c]:
                have += 1

            while have == need:
                if R - L + 1 < length:
                    res = (L,R+1)
                    length = R - L + 1
                left = s[L]
                window[left] -= 1
                L += 1
                if left in freqt and freqt[left] > window[left]:
                    have -= 1
            
        
            
            
        
        return s[res[0]:res[1]] if length != float('inf') else ""
            



