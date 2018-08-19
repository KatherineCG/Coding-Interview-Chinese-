#coding=utf-8
class Solution():
    #排列
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        charlist = list(ss)
        charlist.sort()
        pStr = []
        for i in range(len(charlist)):
            if i > 0 and charlist[i-1] == charlist[i]:
                continue
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i+1:]))
            for j in temp:
                pStr.append(charlist[i] + j)
        return pStr
    #组合
    def group(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        charlist = list(ss)
        charlist.sort()
        pStr = []
        for i in range(len(charlist)):
            pStr.append(charlist[i])
            if i > 0 and charlist[i-1] == charlist[i]:
                continue
            temp = self.group(''.join(charlist[i+1:]))
            for j in temp:
                pStr.append(charlist[i]+j)
        pStr = list(set(pStr))
        pStr.sort()
        return pStr
test = Solution()
ss = 'abc'
#先组合
sgroup = test.group(ss)
result = []
#再排列
for ss in sgroup:
    result += test.Permutation(ss)
print result