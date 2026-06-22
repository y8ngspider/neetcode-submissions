class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)

        ans = 0
        for n in h:
            count =0
            i=n
            while i in h:
                count+=1
                i+=1
            ans=max(count, ans)
        return ans