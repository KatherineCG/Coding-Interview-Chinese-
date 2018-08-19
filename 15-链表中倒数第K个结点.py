# coding=utf-8
import re
class ListNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Solution():
    def __init__(self):
        self.head = None
        
    def GetLastKNode(self, pListHead, k):
        if k <= 0 :
            print ("k Error")
            return
        if pListHead == None:
            print("链表为空")
            return
        if pListHead.next == None and k == 1:
            return pListHead.data
        p = pListHead
        p1 = pListHead
        count1 = 0
        count2 = 0
        while p.next != None:
            count1 += 1
            if count1 - k + 1 > 0:
                count2 = count1 - k + 1
                p1 = p1.next
            p = p.next
        if count1 - k + 1 < 0:
            print ("K大于链表长度")
            return
        else:
            return p1.data

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

input = raw_input()
input  = re.sub('[{}]', '', input).split(',')
k = int(input[0])
node = ListNode(int(input[1]))
p = node
for ch in input[2:]:
    p.next = ListNode(int(ch))
    p = p.next
    
test = Solution()
print '{' + repr(test.GetLastKNode(node, k)) + '}'