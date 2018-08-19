# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        nleft = self.TreeDepth(pRoot.left)
        nright = self.TreeDepth(pRoot.right)
        if nleft > nright:
            return nleft+1
        else:
            return nright+1