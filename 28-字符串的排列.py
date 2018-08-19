# -*- coding:utf-8 -*-
import re
class Solution:
    def Permutation(self, ss):
        # write code here
        result = {}
        if not ss:
            return []
        result = self.PermutationItem(ss, 0, result)
        result[ss] = ss
        return result
    def PermutationItem(self, ss, num, result):
        if num >= len(ss):
            return result
        else:
            result = self.PermutationItem(ss, num + 1, result)
            temp = ss[num]
            data = ss
            for i in range(num+1, len(ss)):
                tempi = ss[i]
                ss = ss[:num] + tempi + ss[num + 1:i] + temp + ss[i + 1:]
                result[ss] = ss
                result = self.PermutationItem(ss, num+1, result)
                ss = data
            return result
        
ss = raw_input()
if ss == '""':
    print []
else:
    test = Solution()
    ss = re.sub('[""]', '', ss)
    str = test.Permutation(ss)
    output = ''
    for i in str:
        output += '"' + str[i] + '"' + ','
    print '[' + output[:len(output)-1] + ']'