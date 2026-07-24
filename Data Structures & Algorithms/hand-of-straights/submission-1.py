class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if cant be divided into equal groups
        if len(hand)%groupSize:
            return False
        
        dic = defaultdict(int)

        for i in hand:
            dic[i] += 1

        
        minH = list(dic.keys())
        heapq.heapify(minH)
    
        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i not in dic:
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


        
