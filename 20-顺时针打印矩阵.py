# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    #！！！！！注意需要的返回值！！！
    def printMatrix(self, matrix):
        # write code here
        res = []
        matrix1 = matrix
        rawnum = len(matrix1)
        if rawnum <= 0:
            return []
        colnum = len(matrix1[0])
        i = 0
        j = 0
        #处理只有一行
        if rawnum == 1:
            for j in range(colnum):
                res.append(matrix[0][j])
        #处理只有一列
        elif colnum == 1:
            for i in range(rawnum):
                res.append(matrix[i][0])
        #处理其他情况
        elif rawnum > 0 and colnum > 0:
            for j in range(colnum):
                res.append(matrix1[0][j])
            for i in range(rawnum-1):
                res.append(matrix1[i+1][j])
            while j > 0 :
                res.append(matrix1[rawnum-1][j-1])
                j -= 1
            while i > 0 :
                res.append(matrix1[i][0])
                i -= 1
            matrix1 = []
            for i in range(1,rawnum-1):
                matrix1.append(matrix[i][1:colnum-1])
            #列表可以直接相加
            res = res + self.printMatrix(matrix1)
        return res

array = input()
test = Solution()
res = test.printMatrix(array)
print res