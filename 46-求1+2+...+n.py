# coding=utf-8
#要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句(A?B:C)
#对列表求和
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1,n+1)))