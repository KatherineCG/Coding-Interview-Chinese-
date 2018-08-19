# coding=utf-8
class Solution():
    def ReOrder(self, data):
        i = 0
        j = len(data) - 1
        while i + 1 != j:
            if (data[i] % 2 == 1) and (data[j] % 2 == 1):
                i += 1
            if (data[i] % 2 == 0) and (data[j] % 2 == 1):
                data[i], data[j] = data[j], data[i]
            if (data[i] % 2 == 1) and (data[j] % 2 == 0):
                j -= 1
            if (data[i] % 2 == 0) and (data[j] % 2 == 0):
                j -= 1
        return data
    #直接用Python的trick，写一个简单的排列数组，顺序不变
    def ReOrder2(self, data):
        left = [x for x in data if x & 1]
        right = [x for x in data if not x & 1]
        return left + right
    # 可扩展性的解法
    # 注意在一个函数的输入中, 输入另一个函数的写法func = self.fucName
    # funcName不需要加括号
    def Order(self, data, func):
        length = len(data)
        if length == 0:
            return
        pBegin = 0
        pEnd = length - 1
        while pBegin + 1 != pEnd:
            while pBegin + 1 != pEnd and not func(data[pBegin]):
                pBegin += 1
            while pBegin + 1 != pEnd and func(data[pEnd]):
                pEnd += 1
            if pBegin + 1 != pEnd:
                data[pBegin], data[pEnd] = data[pEnd], data[pBegin]
        return data
    def isEven(self, n):
        return not n & 0x1
    def ReOrder3(self, data):
        return self.Order(data, self.isEven)
data = [1, 2, 3, 4, 5]
test = Solution()
print(test.ReOrder3(data))
