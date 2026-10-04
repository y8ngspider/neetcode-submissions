class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        res = []
        for idx, n in enumerate(arr):
            if idx > 0 and arr[idx] == arr[idx - 1]:
                continue
            i = idx+1
            j = len(arr) - 1
            diff = -n
            while i < j:
                if arr[i] + arr[j] == diff:
                    res.append([n,arr[i],arr[j]])
                    i+=1
                    j-=1
                    while i < j and arr[i] == arr[i - 1]:
                        i += 1

                    while i < j and arr[j] == arr[j + 1]:
                        j -= 1
                elif arr[i] + arr[j] > diff:
                    j-=1
                else:
                    i+=1
        return res