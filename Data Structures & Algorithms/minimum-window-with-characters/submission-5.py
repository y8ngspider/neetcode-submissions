class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        res = [-1,-1]

        for c in t:
            freq[c] = freq.get(c,0) + 1
        
        window = {}
        have = 0
        need = len(freq)
        l =0
        for r in range(len(s)):
            if s[r] in freq:
                window[s[r]] = window.get(s[r],0) + 1
                if window[s[r]] == freq[s[r]]:
                    have += 1
                
            while have == need:
                if res == [-1,-1] or res[1]-res[0] > (r-l+1):
                    res = [l,r+1] 
                if s[l] in freq:
                    window[s[l]] -= 1
                    if window[s[l]] < freq[s[l]]:
                        have -= 1
                l+=1
            
        return s[res[0]:res[1]] if res != [-1,-1] else ""
