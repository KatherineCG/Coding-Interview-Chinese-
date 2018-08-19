# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
    def FirstAppearingOnce(self):
        # write code here
        res = []
        temp = []
        for ch in self.s:
            if ch not in res and ch not in temp:
                res.append(ch)
            elif ch in res:
                res.remove(ch)
                temp.append(ch)
        if res:
            return res[0]
        else:
            return '#'
    def Insert(self, char):
        # write code here
        self.s += char