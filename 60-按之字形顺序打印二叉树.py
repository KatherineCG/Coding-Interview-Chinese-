# -*- coding:utf-8 -*-
import re
import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        q = Queue.Queue()
        result = []
        q.put(pRoot)
        j = 1
        while not q.empty():
            level = []
            length = q.qsize()
            for i in range(length):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if j%2 == 0:
                print level
                level = level[::-1]
                print level
            result.append(level)
            j += 1
        return result
def HandleInput(data):
    data = re.sub('[{}]', '', data).split(',')
    print data
    pRoot = CreateBinaryTree(data, 0)
    return pRoot
def CreateBinaryTree(data, n):
    if len(data) > 0:
        flag = False
        for i in range(n, len(data)):
            if data[i] != '#':
                flag = True
                break
        if flag:
            l = 2 * n + 1
            r = 2 * n + 2
            if n+1 < len(data) and data[n+1] == '#':
                data.insert(l+2, '#')
                data.insert(r+2, '#')
            if data[n] != '#':
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
    print test.Print(pRootHead)