# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxsum = array[0]
        tempsum = array[0]
        for ch in array[1:]:
            if (tempsum+ch) < ch:
                tempsum = 0
            tempsum += ch
            if tempsum > maxsum:
                maxsum = tempsum
        return maxsum
test = Solution()
array = input()
print test.FindGreatestSumOfSubArray(array)
            