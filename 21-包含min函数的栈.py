#两个栈，一个负责处理输入，一个负责收录最小值，遇到MIN出栈
class Solution():
    def __init__(self):
        self.arr = []
        self.temparr = []
    def push(self, node):
        self.arr.append(node)
    def pop(self):
        return self.arr.pop()
    def temppush(self, node):
        self.temparr.append(node)
    def min(self):
        mininum = self.temparr[-2]
        self.temparr.pop()
        return mininum

test = Solution()
stack = input()
i = 0
output = ''
for ch in stack:
    if ch[:3] == 'PSH':
        test.push(ch[3:])
        if i == 0 or ch[3:] < tempmin:
            tempmin = ch[3:]
        test.temppush(tempmin)
        i += 1
    if ch == 'MIN':
        output = output + tempmin + ','
    if ch == 'POP':
        test.pop()
        tempmin = test.min()
        i -= 1
print (output[:len(output)-1])