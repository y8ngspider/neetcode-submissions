class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        hashmap = {}
        for i in range(len(strs)):
            for j, c in enumerate(strs[i]):
                if j not in hashmap:
                    hashmap[j] = {}
                hashmap[j][c] = hashmap[j].get(c,0) +1
        dobreak = False
        for freq in hashmap.values():
            if dobreak:
                break
            for c, count in freq.items():
                if count == len(strs):
                    res += c
                else:
                    dobreak = True
                    break

        return res

                