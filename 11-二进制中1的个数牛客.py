# -*- coding:utf-8 -*-
'''
如果n=0，返回0
如果n<0,求补码，Python中即为2^32+n
如果n>0，n&1，如果结果为1，则计数器加1，n左移（或者右移）1位
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        count = 0
        if n < 0:
            n = pow(2, 32) + n
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count