class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        L = 0
        longest = 0

        for R in range(len(s)):
            window[s[R]] = window.get(s[R],0) + 1
            while (R - L + 1) - max(window.values()) > k:
                window[s[L]] -=1
                L += 1
            longest = max(R-L+1, longest)
        return longest