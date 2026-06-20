class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width * height
        # width = i-j
        # height = min(heights[i],heights[j])

        # maxArea = max(width*height,maxArea)

        # we know widths are w in range(len(heights))
        # we know that height is 

        l=0
        r=len(heights)-1
        area = 0
        while l<r:
            area = max(area, (r-l)*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            elif heights[r]==heights[l]:
                if heights[r-1] > heights[l+1]:
                    r-=1
                else:
                    l+=1
        return area