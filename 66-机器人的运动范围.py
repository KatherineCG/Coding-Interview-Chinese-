# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        data = [[0 for i in range(cols)] for j in range(rows)]
        count = 0
        count = self.CountNumber(threshold, 0, 0, data)
        return count
    def CountNumber(self, threshold, rows, cols, data):
        row = len(data)
        col = len(data[0])
        if rows < 0 or rows >= row or cols < 0 or cols >= col or data[rows][cols] == 1\
                or self.sum(rows) + self.sum(cols) > threshold:
            return 0
        else:
            data[rows][cols] = 1
            return 1+self.CountNumber(threshold, rows-1, cols, data)\
                   +self.CountNumber(threshold, rows, cols-1, data)\
                   +self.CountNumber(threshold, rows+1, cols, data)\
                   +self.CountNumber(threshold, rows, cols+1, data)
    def sum(self, number):
        result = 0
        while number != 0:
            result += number % 10
            number /= 10
        return result
test = Solution()
threshold = input()
rows = input()
cols = input()
print test.movingCount(threshold, rows, cols)