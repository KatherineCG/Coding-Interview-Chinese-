#-*- coding:utf-8 -*-
import re
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if result == False:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if result == False:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) & self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)

test = Solution()
TreeInput = raw_input()
i = 0
for i in range(0, len(TreeInput)):
    if TreeInput[i] == '}' and TreeInput[i+1] == ',' and TreeInput[i+2] == '{':
        i += 1
        break
    i += 1
pRoot1input = TreeInput[:i]
pRoot2input = TreeInput[i+1:]
def CreateBinaryTree(data, n):
    if len(data) > 0:
        if n < len(data):
            if data[n] != '#':
                l = 2 * n + 1
                r = 2 * n + 2
                root = TreeNode(data[n])
                root.left = CreateBinaryTree(data, l)
                root.right = CreateBinaryTree(data, r)
                return root
            else:
                return None
        else:
            return None
    else:
        return None
    
def HandleInput(array):
    array = re.sub('[{}]', '', array).split(',')
    pRoot = CreateBinaryTree(array, 0)
    return pRoot
def PreOrder(root, RetList):
    if root != None:
        RetList.append(root.val)
    if root.left != None:
        PreOrder(root.left, RetList)
    if root.right != None:
        PreOrder(root.right, RetList)
    return RetList
if pRoot2input == '{}':
    result = False
else:
    if pRoot1input == '{}':
        result = False
    else:
        pRoot1 = HandleInput(pRoot1input)
        pRoot2 = HandleInput(pRoot2input)
        result = test.HasSubtree(pRoot1, pRoot2)
        if result == True:
            print 'true'
        else:
            print 'false'
