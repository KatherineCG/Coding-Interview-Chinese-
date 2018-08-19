# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        length = len(data)
        first = self.GetFirstK(data, k, 0, length-1)
        last = self.GetLastK(data, k, 0, length-1)
        if first != -1 and last != -1:
            return last-first+1
        else:
            return 0
    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        length = len(data)
        mideleIndex = (start + end) / 2
        mideleData = data[mideleIndex]
        if mideleData == k:
            if (mideleIndex < length -1 and data[mideleIndex-1] != k) or mideleIndex == 0:
                return mideleIndex
            else:
                end = mideleIndex - 1
        elif mideleData < k:
            start = mideleIndex + 1
        else:
            end = mideleIndex - 1
        return self.GetFirstK(data, k, start, end)
    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        length = len(data)
        mideleIndex = (start + end) / 2
        mideleData = data[mideleIndex]
        if mideleData == k:
            if (mideleIndex < length -1 and data[mideleIndex+1] != k) or mideleIndex == length-1:
                return mideleIndex
            else:
                start = mideleIndex + 1
        elif mideleData < k:
            start = mideleIndex + 1
        else:
            end = mideleIndex - 1
        return self.GetLastK(data, k, start, end)
test = Solution()
data = input()
k = input()
print test.GetNumberOfK(data, k)
