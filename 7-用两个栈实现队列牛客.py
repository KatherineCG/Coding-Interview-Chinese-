# -*- coding:utf-8 -*-
'''
入队列：直接存入第一个栈
出队列：如果第一个栈不为空，第二个栈为空，则将第一个栈的所有元素先出栈再入栈存入第二个栈，弹出第二个栈顶元素
如果第二个栈元素不为空，直接弹出第二个栈栈顶元素
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        elif len(self.stack1) != 0 and len(self.stack2) == 0:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()