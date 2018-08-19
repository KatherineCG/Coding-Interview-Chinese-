# -*- coding:utf-8 -*-
import re


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #中序遍历二叉搜索树，将结点存入列表中，再为列表中的元素赋值左右指针
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree: return
        self.arr = []
        self.midTraversal(pRootOfTree)
        for i, v in enumerate(self.arr[:-1]):
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v
        return self.arr[0]
    
    #二叉树中序遍历
    def midTraversal(self, root):
        if not root: return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)


def HandleInput(data):
    data = re.sub('[{}]', '', data).split(',')
    pRoot = CreateBinaryTree(data, 0)
    return pRoot


def CreateBinaryTree(data, n):
    if len(data) > 0:
        if n < len(data):
            if data[n] != '#':
                if (n + 3) <= len(data) and data[n + 1] == '#' and data[n + 2] != '#':
                    if n + 3 == len(data) or data[n + 3] == '#':
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
    while pLastNodeInList.right != None:
        resultltor = resultltor + pLastNodeInList.val + ','
        pLastNodeInList = pLastNodeInList.right
    resultltor = resultltor + pLastNodeInList.val + ','
    while pLastNodeInList != None:
        resultrtol = resultrtol + pLastNodeInList.val + ','
        pLastNodeInList = pLastNodeInList.left
    print 'From left to right are:' + resultltor[:len(resultltor) - 1] + ';From right to left are:' + resultrtol[:len(
        resultrtol) - 1] + ';'
