# -*- coding:utf-8 -*-
'''
用两个列表，一个存储奇数，一个存储偶数
返回奇数列表+偶数列表
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return []
        evenres = []
        oddres = []
        for ch in array:
            if ch % 2 == 0:
                evenres.append(ch)
            else:
                oddres.append(ch)
        return oddres + evenres
        