# -*- coding:utf-8 -*-
'''
层次遍历，判断每层是否对称
如果左右结点不存在，队列存入#
根节点不存入队列
'''
import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        q = Queue.Queue()
        if pRoot.left:
            q.put(pRoot.left)
        if pRoot.right:
            q.put(pRoot.right)
        flag = True
        while not q.empty():
            level = []
            length = q.qsize()
            for i in range(length):
                p = q.get()
                if p == '#':
                    level.append(p)
                else:
                    level.append(p.val)
                    if p.left :
                        q.put(p.left)
                    else:
                        q.put('#')
                    if p.right:
                        q.put(p.right)
                    else:
                        q.put('#')
            i = len(level) / 2
            if level[:i] != level[i:][::-1]:
                flag = False
        return flag