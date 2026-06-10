class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        heapq.heapify_max(pq)

        for i in range(len(points)):
            new = (pow(points[i][0],2)+pow(points[i][1],2), points[i])
            heapq.heappush_max(pq,new)
        
        for x in range(len(points)-k):
            heapq.heappop_max(pq)
        
        res=[]
        for j in range(len(pq)):
            res.append(pq[j][1])
        return res
