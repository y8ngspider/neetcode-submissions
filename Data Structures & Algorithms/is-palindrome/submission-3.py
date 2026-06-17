class Solution:
    def isPalindrome(self, s: str) -> bool:        
        res = ""
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                res += s[i]
        L = 0
        R = len(res) - 1    
        while L  < R:
            if res[L] != res[R]:
                return False
            L+=1
            R-=1
        return True