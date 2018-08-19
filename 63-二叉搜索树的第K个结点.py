# -*- coding:utf-8 -*-
#中序遍历第K个结点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None or k <= 0:
            return
        root = []
        res = []
        p = pRoot
        while p != None or root != []:
            while p != None:
                root.append(p)
                p = p.left
            if root != []:
                p = root.pop()
                res.append(p.val)
                p = p.right
        if k > len(res):
            return
        else:
            return res[k-1]
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
print test.KthNode(pRoot, 1)