class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width * height
        # width = i-j
        # height = min(heights[i],heights[j])

        # maxArea = max(width*height,maxArea)

        # we know widths are w in range(len(heights))
        # we know that height is 

        maxArea =0 
        for i in range(len(heights)):
            j = i + 1
            while j < len(heights):               
                curArea = min(heights[j],heights[i])*(j-i)
                maxArea = max(curArea, maxArea)
                j+=1
            print(maxArea)               
        return maxArea