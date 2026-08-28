class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][0]:
                prevHt, prevStart = stack.pop()
                maxArea = max(maxArea, prevHt*(i - prevStart))
                start = prevStart
            stack.append((heights[i],start))
        print(stack)
        for i in range(len(stack)):
            ht, start = stack.pop()
            maxArea = max(maxArea, ht*(len(heights)-start))
        return maxArea

            
            

        


        