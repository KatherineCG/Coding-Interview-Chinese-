# coding=utf-8
import re
class Solution():
    def TwoIntegerPlus(self, num1, num2):
        #两个正数或者两个负数，直接相加
        num1 = list(num1)
        num2 = list(num2)
        if num1[0] != '-' and num2[0] != '-':
            result = self.Add(num1, num2)
        elif num1[0] == num2[0] and num1[0] == '-':
            result = ['-']
            result = result + self.Add(num1[1:], num2[1:])
        elif num1[0] == '-' and num2[0] != '-':
            if len(num1)-1 > len(num2) or (len(num1)-1 == len(num2) and cmp(num1[1:], num2) == 1):
                result = ['-']
                result = result + self.Reduce(num1[1:], num2)
            else:
                result = self.Reduce(num2, num1[1:])
        else:
            if len(num1)-1 > len(num2) or (len(num1)-1 == len(num2) and cmp(num1[1:], num2) == 1):
                result = self.Reduce(num1, num2[1:])
            else:
                result = ['-']
                result = result + self.Reduce(num2[1:], num1)
        
        result = "".join(result)
        return result

    #相加函数
    def Add(self, num1, num2):
        flag= 0
        result = []
        length1 = len(num1)
        length2 = len(num2)
        #从最后一位开始，两个数对应位置相加再加flag，大于9，flag=1
        if length1 > length2:
            num2 = ['0' for i in range(length1 - length2)] + num2
            i = length1 - 1
        elif length2 > length1:
            num1 = ['0' for i in range(length2 - length1)] + num1
            i = length2 - 1
        else:
            i = length1 - 1
        while i >= 0 :
            temp = int(num1[i]) + int(num2[i]) + flag
            if temp > 9:
                flag = 1
                temp = temp - 10
            else:
                flag = 0
            temp = repr(temp)
            result.insert(0,temp)
            i -= 1
        
        return result
        
    #相减函数
    def Reduce(self, num1, num2):
        flag = 0
        result = []
        length1 = len(num1)
        length2 = len(num2)
        if length1 != length2:
            num2 = ['0' for i in range(length1 - length2)] + num2
        i = length1 - 1
        #从最后一位开始，对应位相减再减flag，为负数+10，flag=1，正数flag=0
        while i>=0 :
            temp = int(num1[i]) - int(num2[i]) - flag
            if temp < 0:
                flag = 1
                temp = temp + 10
            else:
                flag = 0
            temp = repr(temp)
            result.insert(0,temp)
            i -= 1
        
        return result
        
test = Solution()
num0 = raw_input()
while not re.match(r'(-)?\d+$', num0):
    print "Input Error, Please input again"
    num0 = raw_input('num0:')
num1 = raw_input()
while not re.match(r'(-)?\d+$', num1):
    print "Input Error, Please input again"
    num1 = raw_input('num1:')
result = test.TwoIntegerPlus(num0, num1)
print(result)