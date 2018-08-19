#coding=utf-8
#AC笔记：函数返回布尔值
class Solution():
    def VerifySquenceOfBST(self, sequence):
        length = len(sequence)
        if length <= 0 or sequence == None:
            return False
        root = sequence[len(sequence)-1]
        for i in range(0, length):
            if sequence[i] > root:
                break
        for j in range(i, length):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < length -1:
            right = self.VerifySquenceOfBST(sequence[i:length-1])
        if left == right and left == True:
            return True
        else:
            return False
sequence = input()
test = Solution()
result = test.VerifySquenceOfBST(sequence)
if result == True:
    print 'true'
else:
    print 'false'