class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify_max(heap)

        for i in range(len(nums)):
            heapq.heappush_max(heap,nums[i])
        
        ans = -1001
        for j in range(k):
            ans = heapq.heappop_max(heap)

        if ans == -1001:
            return None
        
        return ans