class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        total = 0
        for n in nums:
            total += n 
            self.arr.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preR = self.arr[right]
        preL = self.arr[left-1] if left > 0 else 0
        return preR - preL
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)