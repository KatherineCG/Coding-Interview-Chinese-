# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        length = len(numbers)
        if not numbers or length < 1:
            return False
        numbers.sort()
        NumberOfZero = 0
        NumberOfGap = 0
        for i in range(length-1):
            if numbers[i] == 0:
                NumberOfZero += 1
                continue
            if numbers[i] == numbers[i+1]:
                return False
            NumberOfGap += numbers[i+1] - numbers[i] - 1
        if NumberOfZero >= NumberOfGap:
            return True
        else:
            return False
test = Solution()
numbers = input()
print test.IsContinuous(numbers)