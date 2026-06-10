class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        heapq.heapify(pq)

        for i in range(len(stones)):
            heapq.heappush(pq, -stones[i])
        
        while len(pq)>1:
            temp1 = -heapq.heappop(pq)
            temp2 = -heapq.heappop(pq)
            res = temp1-temp2
            if res>0:
                heapq.heappush(pq, -res)
        
        if len(pq)==1:
            return -pq[0]
        return 0
