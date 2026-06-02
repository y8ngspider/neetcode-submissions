class Solution:
    def encode(self, strs: List[str]) -> str:
        #put the length of each str in the list as the first character
        res = ""
        for i in range(len(strs)):
            length = str(len(strs[i]))
            res += length+"#"+strs[i]
        return res
            
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            delim = ""
            while s[i]!="#":
                delim+=s[i]
                i+=1
            i+=1
            delim = int(delim)
            res.append(s[i:i+delim])
            i+=delim
        return res

