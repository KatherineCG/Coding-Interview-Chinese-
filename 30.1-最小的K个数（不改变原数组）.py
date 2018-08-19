# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        result = []
        if tinput == [] or k <= 0 or k > len(tinput):
            return result
        for i in range(len(tinput)):
            if len(result) < k:
                result.append(tinput[i])
                result.sort()
            elif tinput[i] >= result[len(result)-1] and len(result) == k:
                continue
            elif tinput[i] < result[len(result)-1]:
                result.pop()
                result.append(tinput[i])
                result.sort()
        return result
test = Solution()
input = input()
tinput = input[0]
k = input[1]
result = test.GetLeastNumbers_Solution(tinput, k)
print result
            