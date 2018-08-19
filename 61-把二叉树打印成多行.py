# -*- coding:utf-8 -*-
import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        res = []
        q = Queue.Queue()
        q.put(pRoot)
        while not q.empty():
            level = []
            length = q.qsize()
            for i in range(length):
                p = q.get()
                level.append(p.val)
                if p.left != None:
                    q.put(p.left)
                if p.right != None:
                    q.put(p.right)
            res.append(level)
        return res