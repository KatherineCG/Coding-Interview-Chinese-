# -*- coding:utf-8 -*-
'''
使用哈希表存储链表每个结点的random结点
Python中哈希表为字典
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        p = pHead
        Clone = RandomListNode(p.label)
        Clone.next = p.next
        i = 0
        randomdict = {}
        if pHead.random != None:
            randomdict[i] = p.random
        i += 1
        PClone = Clone
        p = p.next
        while p != None:
            pCloned = RandomListNode(p.label)
            pCloned.next = p.next
            if p.random != None:
                randomdict[i] = p.random
            Clone.next = pCloned
            Clone = Clone.next
            p = p.next
            i += 1
        p = PClone
        i = 0
        while p != None:
            if randomdict.has_key(i):
                p.random = randomdict[i]
            i += 1
            p = p.next
        return PClone
test = Solution()
node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node3.random = node1
clonedNode = test.Clone(node1)
while clonedNode != None:
    if clonedNode.random != None:
        print (clonedNode.random.label)
    clonedNode = clonedNode.next