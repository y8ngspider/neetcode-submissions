class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #cars can be divided into fleets based on the number of hours taken to reach
        
        h = {}


        for i in range(len(position)):
            hours = (target-position[i])/speed[i]
            h[position[i]] = hours
        
        h = dict(sorted(h.items(), reverse=True))
        stack = []
        for pos, hrs in h.items():
            if not stack:
                stack.append(hrs)
            elif hrs > stack[-1]:
                stack.append(hrs)
        return len(stack)
