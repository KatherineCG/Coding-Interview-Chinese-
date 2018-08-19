# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers.sort()
        for i in range(0,len(numbers)):
            if i == 0:
                tempnumber = numbers[i]
                temptimes = 1
                if temptimes > len(numbers) / 2:
                    return numbers[i]
            else:
                if numbers[i] == tempnumber:
                    temptimes += 1
                    if temptimes > len(numbers)/2:
                        return numbers[i]
                else:
                    tempnumber = numbers[i]
                    temptimes = 1
        return 0
test = Solution()
numbers = input()
numbers = list(numbers)
print test.MoreThanHalfNum_Solution(numbers)