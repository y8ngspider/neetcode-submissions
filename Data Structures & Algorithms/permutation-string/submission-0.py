class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:      
        freq={}
        ans={}

        for c in s1:
            if c in ans:
                ans[c]+=1
            else:
                ans[c]=1
        L=0
        for R in range(len(s2)):
            if s2[R] in freq:
                freq[s2[R]]+=1
            elif s2[R] not in freq:
                freq[s2[R]]=1
            if (R-L)+1>len(s1):
                freq[s2[L]]-=1
                if freq[s2[L]]==0:
                    del freq[s2[L]]
                L+=1
            if freq == ans:
                return True
        return False
                


            
            
            
                




