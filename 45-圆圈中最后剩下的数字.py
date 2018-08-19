# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0 or m == 0:
            return -1
        array = [i for i in range(n)]
        i = 0
        while len(array) > 1:
            remainder = (m-1) % len(array)
            array = array[remainder+1:] + array[:remainder]
        return array[0]
test = Solution()
n = input()
m = input()
print test.LastRemaining_Solution(n, m)
            
        