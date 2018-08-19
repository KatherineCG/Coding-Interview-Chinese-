# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        length = len(data)
        copy = []
        for i in range(length):
            copy.append(data[i])
        count = self.InverseParisCore(data, copy, 0, length-1)
        return count
    def InverseParisCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return
        length = (end - start) / 2
        left = self.InverseParisCore(copy, data, start, start + length)
        right = self.InverseParisCore(copy, data, start+length+1, end)
        
        i = start + length
        j = end
        indexCopy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j-start-length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count
test = Solution()
data = input()
print data
print test.InversePairs(data)