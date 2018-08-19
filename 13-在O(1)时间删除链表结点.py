# coding=utf-8
class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
    def __del__(self):
        self.data = None
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None
        
        #中间结点
        if pToBeDeleted.next != None:
            p = pToBeDeleted.next
            pToBeDeleted.data = p.data
            pToBeDeleted.next = p.next
            p.__del__()
        #头结点
        elif pToBeDeleted == pListHead:
            pListHead = pToBeDeleted.next
            pToBeDeleted.__del__()
        #尾结点
        else:
            p = pListHead
            while p.next != pToBeDeleted:
                p = p.next
            p.next = None
            pToBeDeleted.__del__()
            
    #输出链表
    def PrintLinkList(self, pListHead):
        while pListHead != None:
            print pListHead.data
            pListHead = pListHead.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

test = Solution()
test.PrintLinkList(node1)
test.DeleteNode(node1, node3)
test.PrintLinkList(node1)
        