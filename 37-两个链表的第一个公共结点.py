# -*- coding:utf-8 -*-
import re
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return
        p1 = pHead1
        p2 = pHead2
        while p1.next != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next
        temphead1 = pHead1
        temphead2 = pHead2
        while p1.next != None:
            temphead1 = temphead1.next
            p1 = p1.next
        while p2.next != None:
            temphead2 = temphead2.next
            p2 = p2.next
        while temphead1.next != None:
            if temphead1.val == temphead2.val:
                return temphead1.val
            else:
                temphead1 = temphead1.next
                temphead2 = temphead2.next
def HandleInput(array):
    pHead = ListNode(array[0])
    pTemp = pHead
    for ch in array[1:]:
        pTemp.next = ListNode(ch)
        pTemp = pTemp.next
    return pHead
array1 = raw_input()
array1 = re.sub('[{}]', '', array1).split(',')
array2 = raw_input()
array2 = re.sub('[{}]', '', array2).split(',')
pHead1 = HandleInput(array1)
pHead2 = HandleInput(array2)
test = Solution()
print test.FindFirstCommonNode(pHead1, pHead2)