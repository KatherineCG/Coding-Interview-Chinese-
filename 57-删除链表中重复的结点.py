# -*- coding:utf-8 -*-
#1.加一个头结点
#2.两个临时指针p,q
#3.找前后不相等的节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        pResHead = ListNode(pHead.val-1)
        tempResHead = pResHead
        same = pHead.val-1
        p = pHead
        while p != None:
            if p.val == same:
                p = p.next
            else:
                same = p.val
                if p.next == None or p.val != p.next.val:
                    tempResHead.next = p
                    tempResHead = tempResHead.next
                p = p.next
        tempResHead.next = None
        return pResHead.next
test = Solution()
def HandleInput(array):
    pHead = ListNode(int(array[0]))
    p = pHead
    for ch in array[1:]:
        p.next = ListNode(int(ch))
        p = p.next
    return pHead
array = raw_input()
pHead = HandleInput(array)
pResHead = test.deleteDuplication(pHead)
while pResHead!=None:
    print pResHead.val
    pResHead = pResHead.next
