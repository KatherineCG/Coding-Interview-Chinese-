# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == None or pattern == None:
            return False
        return self.matchCore(s, pattern)
    def matchCore(self, s, pattern):
        if not s:
            if not pattern:
                return True
            if len(pattern) == 2 and pattern[1] == '*':
                return True
        if not pattern:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if s:
                if pattern[0] == s[0] or pattern[0] == '.' :
                    return self.matchCore(s[1:], pattern[2:]) or self.matchCore(s[1:], pattern) or self.matchCore(s, pattern[2:])
                else:
                    return self.matchCore(s, pattern[2:])
        if s:
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.matchCore(s[1:], pattern[1:])
        return False
test = Solution()
s = raw_input()
pattern = raw_input()
print test.match(s, pattern)