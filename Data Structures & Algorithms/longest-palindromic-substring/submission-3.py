class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        def dfs(i,j,cur):
            if i < 0 or j >= len(s) or s[i] != s[j]:
                return cur
            cur = s[i:j+1]
            return dfs(i-1,j+1,cur)
        
        for i in range(len(s)):
            curword = dfs(i,i,"")
            if len(curword) > len(longest):
                longest = curword
        for i in range(len(s)):
            curword = dfs(i,i+1,"")
            if len(curword) > len(longest):
                longest = curword
            
        return longest

