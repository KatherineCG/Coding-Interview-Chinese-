# -*- coding:utf-8 -*-
import re
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        pLastNodeInList = None
        pLastNodeInList = self.ConvertNode(pRootOfTree, pLastNodeInList)
        pHeadOfList = pLastNodeInList
        while pLastNodeInList != None and pLastNodeInList.left != None:
            pHeadOfList = pLastNodeInList.left
            pLastNodeInList = pLastNodeInList.left
        return pHeadOfList
    def ConvertNode(self, pNode, pLastNodeInList):
        if pNode == None:
            return
        pCurrent = pNode
        if pCurrent.left != None:
            pLastNodeInList = self.ConvertNode(pCurrent.left, pLastNodeInList)
        pCurrent.left = pLastNodeInList
        if pLastNodeInList != None:
            pLastNodeInList.right = pCurrent
        pLastNodeInList = pCurrent
        if pCurrent.right != None:
            pLastNodeInList = self.ConvertNode(pCurrent.right, pLastNodeInList)
        return pLastNodeInList

def HandleInput(data):
    data = re.sub('[{}]', '', data).split(',')
    pRoot = CreateBinaryTree(data, 0)
    return pRoot
def CreateBinaryTree(data, n):
    if len(data) > 0:
        if n < len(data):
            if data[n] != '#':
                if (n+3) <= len(data) and data[n+1] == '#' and data[n+2] != '#':
                    if n+3 == len(data) or data[n+3] == '#':
                        l = n + 2
                        r = n + 3
                else:
                    l = 2 * n + 1
                    r = 2 * n + 2
                pRoot = TreeNode(data[n])
                pRoot.left = CreateBinaryTree(data, l)
                pRoot.right = CreateBinaryTree(data, r)
                return pRoot
            else:
                return None
        else:
            return None
    else:
        return None
inputarray = raw_input()
test = Solution()
resultltor = ''
resultrtol = ''
if inputarray == '{}':
    print None
else:
    pRootHead = HandleInput(inputarray)
    pLastNodeInList = test.Convert(pRootHead)
    while pLastNodeInList.left != None:
        resultrtol = resultrtol + pLastNodeInList.val + ','
        pLastNodeInList = pLastNodeInList.left
    resultrtol = resultrtol + pLastNodeInList.val + ','
    while pLastNodeInList != None:
        resultltor = resultltor + pLastNodeInList.val + ','
        pLastNodeInList = pLastNodeInList.right
    print 'From left to right are:' + resultltor[:len(resultltor)-1] + ';From right to left are:' + resultrtol[:len(resultrtol) - 1] + ';'