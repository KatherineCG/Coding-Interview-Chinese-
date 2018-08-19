# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        result = []
        small = 1
        big = 2
        middle = (1+tsum) / 2
        tempresult = [1]
        while small < middle:
            if sum(tempresult) == tsum:
                temp = tempresult[:]
                result.append(temp)
                tempresult.append(big)
                big += 1
            elif sum(tempresult) < tsum:
                tempresult.append(big)
                big += 1
            else:
                tempresult.pop(0)
                small += 1
        return result
test = Solution()
tsum = input()
print test.FindContinuousSequence(tsum)