'''
class Solution():
    def perm (self, n, begin, end, result):
        if begin >= end:
            result.append(repr(n))
            return result
        else:
            i = begin
            for num in range(begin, end):
                n[num], n[i] = n[i], n[num]
                result = self.perm(n, begin+1, end, result)
                n[num], n[i] = n[i], n[num]
            return result
'''
class Solution():
    def Permutation(self, ss):
        result = []
        if not ss:
            return []
        else:
            end = len(ss)
            result = self.perm(ss, 0 , end, result)
            return result
    def perm(self, ss, begin, end, result):
        if begin >= end:
            length = len(result)
            result.append(ss)
            for ch in result[:length]:
                if ss == ch:
                    result.pop()
            return result
        else:
            temp = ss[begin]
            data = ss
            for i in range(begin, end):
                tempi = ss[i]
                if begin != i:
                    ss = ss[:begin] + tempi + ss[begin+1:i] + temp + ss[i+1:]
                result = self.perm(ss, begin+1, end ,result)
                ss = data
            return result
test = Solution()
n = 'abc'
result = []
result = test.perm(n, 0, len(n), result)
print result