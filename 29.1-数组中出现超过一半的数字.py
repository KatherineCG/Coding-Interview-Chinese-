# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if self.CheckInvalidArray(numbers):
            return 0
        number = numbers[0]
        times = 1
        for i in range(1,len(numbers)):
            if numbers[i] == number:
                times += 1
            else:
                times -= 1
            if times == 0:
                number = numbers[i]
                times = 1
        if self.ChedkMoreThanHalf(numbers, number):
            return number
        else:
            return 0
    def CheckInvalidArray(self, numbers):
        g_bInputInvalid = False
        if numbers == [] and len(numbers) <= 0 :
            g_bInputInvalid = True
        return g_bInputInvalid
    def ChedkMoreThanHalf(self, numbers, number):
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == number:
               times += 1
        if times > len(numbers)/2:
            return True
        else:
            return False
test = Solution()
numbers = input()
print test.MoreThanHalfNum_Solution(numbers)