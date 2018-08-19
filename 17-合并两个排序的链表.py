# coding=utf-8
import re
class ListNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pMergeHead = pHead1
        while pHead1 != None and pHead2 != None:
            if pHead1.data <= pHead2.data:
                if pHead1.next and pHead1.next.data >= pHead2.data:
                    pHead1_next = pHead1.next
                    pHead2_next = pHead2.next
                    pHead1.next = pHead2
                    pHead2.next = pHead1_next
                    pHead1 = pHead1_next
                    pHead2 = pHead2_next
                elif pHead1.next == None:
                    pHead1.next = pHead2
                    break
                else:
                    pHead1 = pHead1.next
            else:
                pHead2 = pHead2.next
        if pHead2 != None:
            pHead1 = pHead2
        return pMergeHead

test = Solution()
input = raw_input()
i = 0
for i in range(0, len(input)):
    if input[i] == '}' and input[i+1] == ',' and input[i+2] == '{':
        i += 1
        break
    i += 1
pHead1input = input[:i]
pHead2input = input[i+1:]
def HandleInput(array):
    array = re.sub('[{}]', '', array).split(',')
    pHead = ListNode(int(array[0]))
    p = pHead
    for ch in array[1:]:
        p.next = ListNode(int(ch))
        p = p.next
    return pHead
if pHead1input == '{}' and pHead2input == '{}':
    print '{}'
else:
    if pHead1input == '{}' and pHead2input != '{}':
        pMergeHead = HandleInput(pHead2input)
    elif pHead1input != '{}' and pHead2input == '{}':
        pMergeHead = HandleInput(pHead1input)
    else:
        pHead1 = HandleInput(pHead1input)
        pHead2 = HandleInput(pHead2input)
        if pHead1.data <= pHead2.data:
            pMergeHead = test.Merge(pHead1, pHead2)
        else:
            pMergeHead = test.Merge(pHead2, pHead1)
    output = '{'
    while pMergeHead != None:
        output = output + repr(pMergeHead.data)
        if pMergeHead.next != None:
            output = output + ','
        pMergeHead = pMergeHead.next
    print output + '}'
