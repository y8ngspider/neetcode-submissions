class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1
        res = []
        dic = dict(sorted(dic.items(), key=lambda item: item[1],reverse=True))
        x = list(dic.keys())
        for i in range(k):
            res.append(x[i])
        return res

