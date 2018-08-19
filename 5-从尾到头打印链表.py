# coding=utf-8

from __future__ import print_function

class ListNode:
    def __init__(self, data, next):
        self.val = data
        self.next = next

class HandleListNode:
    def __init__(self):
        self.root = None

    def addNode(self, data):
        if self.root == None:
            self.root = ListNode(data=data, next=None)
            return self.root
        else:
            # 有头结点，则需要遍历到尾部节点，进行链表增加操作
            cursor = self.root
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = ListNode(data=data, next=None)
            return self.root

    # 打印链表自身元素
    def printlistnode(self):
        if(self.root==None):
            return
        else:
            cursor = self.root
            while cursor!=None:
                print(cursor.val, end=' ')
                cursor = cursor.next
            print()

    #求链表的长度
    def size(self):
        if self.root == None:
            return
        else:
            cur = self.root
            count = 1
            while cur.next != None:
                count += 1
                cur = cur.next
        return count

    def reverse(self):
        if self.root == None:
            return
        if self.size() == 1:
            return
        else:
            pre = None
            cursor = self.root
            while cursor != None:
                post = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = post
            self.root = pre

    #逆序思路2：递归

class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

#if __name__ == '__main__':
listnode = HandleListNode()
l1_list = [1,8,3]

for i in l1_list:
    l1 = listnode.addNode(i)

listnode.printlistnode()
listnode.reverse()
listnode.printlistnode()
print (listnode.size())
#test = Solution()
#print (test.printListFromTailToHead(l1))
