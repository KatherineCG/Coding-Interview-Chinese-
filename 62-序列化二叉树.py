# -*- coding:utf-8 -*-
import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if root == None:
            return []
        res = []
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            length = q.qsize()
            for i in range(length):
                p = q.get()
                if p == '#':
                    res.append('#')
                else:
                    res.append(p.val)
                    if p.left != None:
                        q.put(p.left)
                    else:
                        q.put('#')
                    if p.right != None:
                        q.put(p.right)
                    else:
                        q.put('#')
        return res
    def Deserialize(self, s):
        # write code here
        pRoot = self.CreateBinaryTree(s, 0)
        return pRoot
    def CreateBinaryTree(self, data, n):
        if len(data) > 0:
            flag = False
            for i in range(n, len(data)):
                if data[i] != '#':
                    flag = True
                    break
            if flag:
                l = 2 * n + 1
                r = 2 * n + 2
                j = n + 1
                if j < len(data):
                    while data[j] == '#':
                        if data[j:] == ['#' for x in range(j, len(data))] :
                            break
                        data.insert(l + 2*(j-n), '#')
                        data.insert(r + 2*(j-n), '#')
                        j += 1
                if data[n] != '#':
                    pRoot = TreeNode(data[n])
                    pRoot.left = self.CreateBinaryTree(data, l)
                    pRoot.right = self.CreateBinaryTree(data, r)
                    return pRoot
                else:
                    return None
            else:
                return None
        else:
            return None
test = Solution()
s = raw_input().split(',')
pRoot = test.Deserialize(s)
print test.Serialize(pRoot)