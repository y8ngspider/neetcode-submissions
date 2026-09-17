class Solution:
    def isPalindrome(self, s: str) -> bool:        
        res = s.lower()

        i = 0
        j = len(s) - 1

        while i <= j:
            if not res[i].isalnum():
                i+=1
            elif not res[j].isalnum():
                j-=1
            elif res[i] != res[j]:
                return False
            else:
                i+=1
                j-=1
        return True