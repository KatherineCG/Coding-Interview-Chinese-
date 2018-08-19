# -*- coding:utf-8 -*-
#先说个定理：两个指针一个fast、一个slow同时从一个链表的头部出发
#fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇
#此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
#这次两个指针一次走一步，相遇的地方就是入口节点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None:
            return None
        pFast = pHead
        pSlow = pHead
        while pFast.next != None:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if pFast.next == None:
            return None
        pSlow = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast.val
test = Solution()
def HandleInput(array):
    pHead = ListNode(int(array[0]))
    p = pHead
    for ch in array[1:]:
        p.next = ListNode(int(ch))
        p = p.next
    p.next = pHead.next
    return pHead
array = raw_input()
pHead = HandleInput(array)
print test.EntryNodeOfLoop(pHead)