class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def inqueue(self, node):
        if len(self.queue2) == None:
            self.queue1.append(node)
        else:
            self.queue2.append(node)

    def outqueue(self):
        if len(self.queue2) == 0 and len(self.queue1) == 0:
            return
        elif len(self.queue2) == 0:
            for i in range(len(self.queue1)-1) :
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            for i in range(len(self.queue2)-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()


Q = Solution()
Q.inqueue(1)
Q.inqueue(2)
Q.inqueue(3)
print Q.outqueue()
Q.inqueue(4)
print Q.outqueue()
print Q.outqueue()
print Q.outqueue()