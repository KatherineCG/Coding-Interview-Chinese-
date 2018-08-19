# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        result = 0
        if not s:
            return 0
        if s.isdigit():
            result = self.StrToIntNumber(s)
        elif s[0] == '+' :
            result = self.StrToIntNumber(s[1:])
        elif s[0] == '-':
            result = - + self.StrToIntNumber(s[1:])
        else:
            return 0
        return result
            
    def StrToIntNumber(self, s):
        result = 0
        j = 0
        for i in range(len(s))[::-1]:
            result += int(s[i])*pow(10,j)
            j += 1
        return result
test = Solution()
s = raw_input()
print test.StrToInt(s)
        
        
        