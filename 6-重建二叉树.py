# coding=utf-8
from __future__ import print_function
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Solution:
    def __init__(self):
        self.root = None
    #完全二叉树输入
    def add(self, data, Node):
        node = TreeNode(data)
        if Node == None:
            Node = node
        else:
            q = [Node]
            while True:
                pop_node = q.pop(0)
                if pop_node.lchild == None:
                    pop_node.lchild = node
                    return Node
                elif pop_node.rchild == None:
                    pop_node.rchild = node
                    return Node
                else:
                    q.append(pop_node.lchild)
                    q.append(pop_node.rchild)

    #二叉树输出：层次遍历
    def traverse(self, retList, node):
        if node == None:
            return None
        q = [node]
        retList.append(node)
        while q!= []:
            pop_node = q.pop(0)
            if pop_node.lchild is not None:
                q.append(pop_node.lchild)
                retList.append(pop_node.lchild)
            if pop_node.rchild is not None:
                q.append(pop_node.rchild)
                retList.append(pop_node.rchild)
        return retList
    #二叉树输出：前序遍历
    def preorder(self, retList, node):
        if node == None:
            return []
        retList.append(node)
        self.preorder(retList, node.lchild)
        self.preorder(retList, node.rchild)
        return retList

    #二叉树输出：中序遍历
    def inorder(self, retList, node):
        if node == None:
            return []
        self.inorder(retList, node.lchild)
        retList.append(node)
        self.inorder(retList, node.rchild)
        return retList

    #二叉树输出：后序遍历
    def postorder(self, retList, node):
        if node == None:
            return []
        self.postorder(retList, node.lchild)
        self.postorder(retList, node.rchild)
        retList.append(node)
        return retList

    #重构二叉树函数
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.lchild = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.rchild = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root



'''
prearray = raw_input()
pre = prearray.split()


tinarray = raw_input()
tin = tinarray.split()
'''

pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 6, 8]
RetList = []
#newTree = BTree()
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)
preretlist = test.preorder([],newTree)
inretlist = test.inorder([],newTree)
postretlist = test.postorder([],newTree)

newTree = test.add(10, newTree)
#print (newTree)
traretlist = test.traverse([], newTree)

for i in preretlist:
    print (i.data, end=' ')
print ()

for i in inretlist:
    print (i.data, end=' ')
print ()

for i in postretlist:
    print (i.data, end=' ')
print ()

for i in traretlist:
    print (i.data, end=' ')
print ()

