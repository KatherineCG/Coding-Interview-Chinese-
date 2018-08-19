import re
class ListNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Solution():
    def ReverseList(self, pHead):
        if pHead == None:
            return
        p_pre = None
        p = pHead
        while p != None:
            p_next = p.next
            if p_next == None:
                pReversedHead = p
            p.next = p_pre
            p_pre = p
            p = p_next
        return pReversedHead
input = raw_input()
if input == '{}':
    pHead = None
else:
    input = re.sub('[{}]', '', input).split(',')
    pHead = ListNode(int(input[0]))
    p = pHead
    for ch in input[1:]:
        p.next = ListNode(int(ch))
        p = p.next
test = Solution()
ReversepHead = test.ReverseList(pHead)
printarray = '{'
while ReversepHead != None:
    printarray = printarray + repr(ReversepHead.data)
    if ReversepHead.next != None:
        printarray = printarray + ','
    ReversepHead = ReversepHead.next
print printarray + '}'
