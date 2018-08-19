# -*- coding:utf-8 -*-
#用两个字典，代表哈希表
#一个存储每个字符的数量，一个存储只出现一次的字符的位置
#从位置字典中选取位置最小值作为输出
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        temp = {}
        temp1 = {}
        for i in range(len(s)):
            if temp.has_key(s[i]):
                temp[s[i]] += 1
            else:
                temp[s[i]] = 1
            if temp[s[i]] == 1:
                temp1[s[i]] = i
            elif temp1.has_key(s[i]):
                del temp1[s[i]]
        result = len(s)
        for key in temp1:
            if temp1[key] <= result:
                result = temp1[key]
                continue
        return result
test = Solution()
s = raw_input()
print test.FirstNotRepeatingChar(s)