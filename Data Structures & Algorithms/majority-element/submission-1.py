class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0)+1

        for n,freq in freq.items():
            if freq > len(nums)/2:
                return n