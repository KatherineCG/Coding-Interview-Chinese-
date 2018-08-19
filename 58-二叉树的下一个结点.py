# -*- coding:utf-8 -*-
'''
思路：
（1） 若该节点存在右子树：则下一个节点为右子树最左子节点（如图节点 B ）
（2） 若该节点不存在右子树：这时分两种情况：
2.1 该节点为父节点的左子节点，则下一个节点为其父节点（如图节点 D ）
2.2 该节点为父节点的右子节点，则沿着父节点向上遍历，
知道找到一个节点的父节点的左子节点为该节点，则该节点的父节点下一个节点
（如图节点 I ，沿着父节点一直向上查找找到 B （ B 为其父节点的左子节点），
则 B 的父节点 A 为下一个节点）。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        if pNode.right :
            nextNode = pNode.right
            while nextNode.left != None :
                nextNode = nextNode.left
        elif pNode.next and pNode.right == None:
            if pNode == pNode.next.left:
                nextNode = pNode.next
            else:
                nextNode = pNode.next
                while nextNode.next and nextNode != nextNode.next.left:
                    nextNode = nextNode.next
                nextNode = nextNode.next
        else:
            nextNode = None
        return nextNode
        