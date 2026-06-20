class Solution:
    def trap(self, height: List[int]) -> int:
        #what do we have to find?
        pre = []
        suf = [0]*len(height)

        curMax=0
        for i in range(len(height)):
            if i == 0:
                pre.append(0)
                continue
            curMax = max(height[i-1], curMax)
            pre.append(curMax)
        curMax=0
        
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                suf[i]=0
                continue
            curMax = max(height[i+1], curMax)
            suf[i] = curMax
        
        ans=0
        for i in range(len(height)):
            lmax = pre[i]
            rmax = suf[i]
            if height[i]>=min(lmax,rmax):
                continue
            else:
                ans+=min(lmax,rmax)-height[i]
        
        return ans

