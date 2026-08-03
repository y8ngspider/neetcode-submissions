class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N,M = len(word1), len(word2)
        cache = [[-1] * M for _ in range(N)]

        def dfs(s1, s2, i1, i2):
            if i1 == len(s1):
                return len(s2) - i2
            if i2 == len(s2):
                return len(s1) - i1
            if cache[i1][i2] != -1:
                return cache[i1][i2]
            if s1[i1] == s2[i2]:
                cache[i1][i2] = 0 + dfs(s1,s2,i1+1,i2+1)
            else:
                cache[i1][i2] = min(1+dfs(s1,s2,i1,i2+1),1+dfs(s1,s2,i1+1,i2), 1 + dfs(s1,s2,i1 + 1, i2 + 1))
            return cache[i1][i2]
        
        return dfs(word1,word2,0,0)