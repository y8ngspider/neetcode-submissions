class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window = set()
        length = 0
        for R in range(len(s)):
            while s[R] in window and L <= R:
                window.remove(s[L])
                L+=1
            window.add(s[R])
            length = max(length,R-L+1)
        
        return length