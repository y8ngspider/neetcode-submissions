class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = [False, False, False]

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if x == target[0]:
                    a[0] = True
                if y == target[1]:
                    a[1] = True
                if z == target[2]:
                    a[2] = True
            if a == [True, True, True]:
                return a == [True, True, True]


        return a == [True, True, True]