# coding=utf-8
#把一个整数减去1，再和原来的整数做与运算，会把该证书最后边一个1变成0.
#那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
#例：1100 -> 1100-1=1011 -> 1100&1011=1000 -> 1000-1=0111 -> 1000&0111=0000
#负数用其补码表示，先与0xFFFFFFFF做与运算，再加1
class Solution():
    def NumberOf1(self, n):
        count = 0
        while(n):
            count += 1
            n = (n - 1) & n
        return count
    #按照计算机中有32位存储
    def NumberOf1_1(self, n):
        num = bin(n).replace('0b', '')
        if num[0] == '-':
            return 32 - num.count('0')
        else:
            return num.count('1')
    
    def powerOf2(self, n):
        if n <= 0:
            return False
        elif n & (n-1) == 0:
            return True
        
    def andor(self, m, n):
        num = m ^ n
        numlist = bin(num).replace('0b', '')
        return numlist.count('1')
    
    def andor1(self, m, n):
        diff = m ^ n
        count = 0
        while(diff):
            count += 1
            diff = diff & (diff - 1)
        return count
if __name__ == '__main__':
    test = Solution()
    print test.NumberOf1(127)
    #print test.NumberOf1(-127)
    print test.NumberOf1(0)
    #print test.NumberOf1(-1)
    print test.NumberOf1_1(127)
    print test.NumberOf1_1(-127)
    print test.NumberOf1_1(0)
    print test.NumberOf1_1(-1)
    print test.powerOf2(0)
    print test.andor(10, 13)
    print test.andor1(10, 13)