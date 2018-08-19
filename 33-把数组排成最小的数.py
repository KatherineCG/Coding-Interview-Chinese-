# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            minnum = ''
        else:
            length = len(numbers)
            numbers = map(str, numbers)
            self.Compare(numbers, 0, length-1)
            minnum = ''.join(numbers)
        return minnum
    def Compare(self, numbers, start, end):
        if start >= end:
            return numbers
        key = numbers[start]
        low = start
        high = end
        while start < end :
            while start < end and int(key + numbers[end]) <= int(numbers[end] + key):
                end -= 1
            while start < end and int(key + numbers[end]) > int(numbers[end] + key):
                numbers[start] = numbers[end]
                start += 1
                numbers[end] = numbers[start]
        numbers[start] = key
        self.Compare(numbers, low, start)
        self.Compare(numbers, start+1, high)
        return numbers
        
test = Solution()
numbers = input()
print test.PrintMinNumber(numbers)