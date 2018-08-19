# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        result = []
        if tinput == [] or k > len(tinput):
            return result
        tinput.sort()
        for i in range(k):
            result.append(tinput[i])
        return result
test = Solution()
input = input()
tinput = input[0]
k = input[1]
result = test.GetLeastNumbers_Solution(tinput, k)
print result