# -*- coding:utf-8 -*-
from operator import mul
class Solution:
    def multiply(self, A):
        # write code here
        if not A :
            return
        A1,B = [], []
        length = len(A)
        for i in range(length):
            A1 = A[:i] + A[i+1:]
            B.append(reduce(mul, A1))
        return B
test = Solution()
A = input()
print test.multiply(A)