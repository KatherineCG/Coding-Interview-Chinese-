# -*- coding:utf-8 -*-
#平衡二叉树：左右子树的深度相差不超过1
import re
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.maxDepth(pRoot.left) - self.maxDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    
    def maxDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.maxDepth(pRoot.left), self.maxDepth(pRoot.right)) + 1

def HandleInput(data):
    data = re.sub('[{}]', '', data).split(',')
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
            if data[n+1] == '#':
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
    print test.IsBalanced_Solution(pRootHead)
        