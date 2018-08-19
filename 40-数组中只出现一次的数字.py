# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        length = len(array)
        if not array or length < 2:
            return
        resultExclusiveOR = 0
        for i in range(length):
            resultExclusiveOR ^= array[i]
        indexOf1 = 0
        while resultExclusiveOR & 1 != 1:
            resultExclusiveOR = resultExclusiveOR >> 1
            indexOf1 += 1
        data1 = 0
        data2 = 0
        for i in range(length):
            if self.IsBit1(array[i], indexOf1):
                data1 ^= array[i]
            else:
                data2 ^= array[i]
        result = [data1, data2]
        return result
    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1