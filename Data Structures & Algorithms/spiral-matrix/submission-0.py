class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lb,rb = 0,len(matrix[0])
        tb,bb = 0, len(matrix)
        res = []
        while lb < rb and tb < bb:

            #top row
            for i in range(lb,rb):
                res.append(matrix[tb][i])
            tb+=1
            #right col
            for i in range(tb,bb):
                res.append(matrix[i][rb-1])
            rb-=1
            
            if not (lb < rb and tb < bb):
                break

            #bottom row
            for i in range(rb-1,lb-1,-1):
                res.append(matrix[bb-1][i])
            bb-=1
            #left col
            for i in range(bb-1,tb-1,-1):
                res.append(matrix[i][lb])
            lb+=1
        return res

            