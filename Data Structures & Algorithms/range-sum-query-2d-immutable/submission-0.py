class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr = []
        for r in range(len(matrix)):
            total = 0
            new = []
            for n in matrix[r]:
                total +=n
                new.append(total)
            self.arr.append(new)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for r in range(row1, row2 +1):
            preR = self.arr[r][col2]
            preL = self.arr[r][col1-1] if col1 > 0 else 0
            sum += preR - preL

        return sum


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)