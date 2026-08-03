class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1), len(text2)
        cache = [[-1] * M for _ in range(N)]
        def dfs(text1, text2, i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if cache[i1][i2] != -1:
                return cache[i1][i2]

            if text1[i1] == text2[i2]:
                cache[i1][i2] = 1 + dfs(text1, text2, i1+1, i2+1)
            
            else:
                cache[i1][i2] = max(dfs(text1, text2, i1, i2+1), dfs(text1, text2, i1+1, i2))
            return cache[i1][i2]
            
        return dfs(text1, text2, 0,0)

        