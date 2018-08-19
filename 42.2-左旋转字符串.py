# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return s
        for i in range(n):
            s += s[i]
        s = s[n:]
        return s
test = Solution()
s = raw_input()
print test.LeftRotateString(s, 3)