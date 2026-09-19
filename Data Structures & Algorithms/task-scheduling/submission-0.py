class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        maxHeap = []
        heapq.heapify_max(maxHeap)
        for task in tasks:
            freq[task] = 1 + freq.get(task,0)

        for task, count in freq.items():
            heapq.heappush_max(maxHeap,(count,task))
        
        min_cycle = 0
        while maxHeap:
            i = n + 1
            arr = []
            while i > 0 and maxHeap:
                count, task = heapq.heappop_max(maxHeap)
                arr.append(task)
                freq[task] -= 1
                i -= 1
            for task in arr:
                if freq[task] > 0:
                    heapq.heappush_max(maxHeap,(freq[task],task))
            if maxHeap:
                min_cycle += n + 1
            else:
                min_cycle += len(arr)
        return min_cycle

        
