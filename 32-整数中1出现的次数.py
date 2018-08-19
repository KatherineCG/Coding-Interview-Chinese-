# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0:
            return 0
        #n = str(n)
        return self.NumberOf1(n)
    def NumberOf1(self, n):
        if n == '' or (not n.isdigit()):
            return 0
        first = int(n[0])
        length = len(n)
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1
        
        numFirstDigit = 0
        if first > 1:
            numFirstDigit = self.PowerBase10(length-1)
        elif first == 1:
            numFirstDigit = int(n[1:]) + 1
        
        numOtherDigits = first * (length-1) * self.PowerBase10(length-2)
        
        numRescursive = self.NumberOf1(n[1:])
        
        return numFirstDigit + numOtherDigits + numRescursive
    
    def PowerBase10(self, n):
        result = 1
        for i in range(n):
            result *= 10
        return result

test = Solution()
n = raw_input()
print test.NumberOf1Between1AndN_Solution(n)