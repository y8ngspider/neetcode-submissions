class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[]
        idx=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            n=temperatures[i]
            while stack and n > stack[-1]:
                stack.pop()
                j = idx.pop()
                res[j]=i-j
            stack.append(n)
            idx.append(i)
        return res    
            

