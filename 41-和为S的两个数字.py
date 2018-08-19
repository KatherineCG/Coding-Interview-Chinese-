# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i = 0
        j = len(array)-1
        result = []
        while i < j:
            sum = int(array[i]) + int(array[j])
            if sum == tsum:
                multi = int(array[i]) * int(array[j])
                if result == []:
                    tempmulti = multi
                    result.append(int(array[i]))
                    result.append(int(array[j]))
                elif multi < tempmulti:
                    tempmulti = multi
                    result.append(int(array[i]))
                    result.append(int(array[j]))
                i += 1
                j -= 1
            elif sum < tsum:
                i += 1
            else:
                j -= 1
        return result
test = Solution()
array = raw_input()
tsum = input()
array = array.split(',')
print test.FindTwoNumbers(array, tsum)
