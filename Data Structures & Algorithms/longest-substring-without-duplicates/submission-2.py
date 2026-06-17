class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        window = set()
        for R in range(len(s)):
            if s[R] not in window:
                length = max(length, R-L+1)
            while s[R] in window:
                window.remove(s[L])
                L+=1
            window.add(s[R])
                         
        return length

