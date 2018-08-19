# coding=utf-8
class Solution:

    #建立新字符串
    def Replace1(self, s):
        tempstr = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                tempstr += '%20'
            else:
                tempstr += c
        return tempstr

    #直接在原字符串替换
    def Replace2(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    #
    def Replace3(self, s):
        if not isinstance(s, str) and len(s) <= 0 and s == None:
            return
        spacenum = 0
        for i in s:
            if i == ' ':
                spacenum += 1
        newStrLen = len(s) + 2*spacenum
        newStr = newStrLen * [None]
        indexOfOriginal = len(s) - 1
        indexOfNew = newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return "".join(newStr)


replacespace = Solution()
array = raw_input()
print (replacespace.Replace1(array))
print (replacespace.Replace2(array))
print (replacespace.Replace3(array))

