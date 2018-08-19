# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = s.split(' ')
        result = []
        for ch in s[::-1]:
            result.append(ch)
        result = ' '.join(result)
        return result
test = Solution()
array = raw_input()
print test.ReverseSentence(array)