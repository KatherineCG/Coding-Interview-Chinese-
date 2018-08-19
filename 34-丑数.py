# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <=0 :
            return 0
        uglynumber = [1]
        Q2 = []
        Q3 = []
        Q5 = []
        i = 0
        flag = True
        length = len(uglynumber)
        while length < index:
            if flag:
                Q2.append(uglynumber[length-1]*2)
                Q3.append(uglynumber[length-1] * 3)
                Q5.append(uglynumber[length-1] * 5)
            if Q2[0] == min(Q2[0],Q3[0],Q5[0]):
                if Q2[0] > uglynumber[length-1]:
                    uglynumber.append(Q2[0])
                    flag = True
                Q2.pop(0)
            elif Q3[0] == min(Q2[0],Q3[0],Q5[0]):
                if Q3[0] > uglynumber[length-1]:
                    uglynumber.append(Q3[0])
                    flag = True
                else:
                    flag = False
                Q3.pop(0)
            elif Q5[0] == min(Q2[0],Q3[0],Q5[0]):
                if Q5[0] > uglynumber[length-1]:
                    uglynumber.append(Q5[0])
                    flag = True
                else:
                    flag = False
                Q5.pop(0)
            length = len(uglynumber)
        return uglynumber[index-1]
test = Solution()
index = input()
print test.GetUglyNumber_Solution(index)
