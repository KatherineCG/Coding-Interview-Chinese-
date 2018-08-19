# -*- coding:utf-8 -*-
'''
# 超时
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.rectCover(number - 1) + self.rectCover(number - 2)
'''
class Solution:
    def rectCover(self, number):
        res = [0,1,2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]