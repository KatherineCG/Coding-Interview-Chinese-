# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == [[]]:
            return False
        row = len(array)
        col = len(array[0])
        if target < array[0][0] or target > array[row-1][col-1]:
            return False
        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True
        return False