# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        result = []
        for ch in numbers:
            if ch in result:
                duplication.append(ch)
                return True
            result.append(ch)
        return False
test = Solution()
numbers = input()
duplication = []
print test.duplicate(numbers, duplication)
print duplication[0]