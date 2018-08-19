class Solution():
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        charlist = list(ss)
        charlist.sort()
        pStr = []
        for i in range(len(ss)):
            if i > 0 and charlist[i-1] == charlist[i]:
                continue
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i+1:]))
            for j in temp:
                pStr.append(charlist[i]+j)
        return pStr
test = Solution()
ss = '12341234'
result = test.Permutation(ss)
#print result
for str in result:
    isTrue1 = str[0]+str[1]+str[2]+str[3] == str[4]+str[5]+str[6]+str[7]
    isTrue2 = str[0]+str[2]+str[4]+str[6] == str[1]+str[3]+str[5]+str[7]
    isTrue3 = str[0]+str[1]+str[4]+str[5] == str[2]+str[3]+str[6]+str[7]
    if isTrue1 and isTrue2 and isTrue3:
        print str