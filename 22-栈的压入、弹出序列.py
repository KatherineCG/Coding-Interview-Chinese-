# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        tempstack = []
        for ch in pushV:
            tempstack.append(ch)
            while tempstack != []:
                if tempstack[-1] == popV[0]:
                    popV = popV[1:]
                    tempstack.pop()
                else:
                    break
        if tempstack ==[] and popV ==[]:
            result = 'true'
        else:
            result = 'false'
        return result
test = Solution()
Vinput = input()
pushV = Vinput[0]
popV = Vinput[1]
print test.IsPopOrder(pushV, popV)