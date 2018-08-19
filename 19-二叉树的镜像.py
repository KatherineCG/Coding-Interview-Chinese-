# coding=utf-8
import re
import Queue
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return
        root_left = root.left
        root.left = root.right
        root.right = root_left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

def HandleInput(array):
    array = re.sub('[{}]', '', array).split(',')
    pRoot = CreateBinaryTree(array, 0)
    return pRoot
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
def TraverseBinaryTree(root):
    res = ''
    q = Queue.Queue()
    if root != None:
        q.put(root)
    while not q.empty():
        length = q.qsize()
        for i in range(length):
            node = q.get()
            res = res + node.val + ','
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
    return res
test = Solution()
input = raw_input()
if input == '{}':
    root = None
else:
    root = HandleInput(input)
    mirrorroot = test.Mirror(root)
    res = TraverseBinaryTree(mirrorroot)
    output = '{' + res[:len(res)-2] + res[len(res)-2] + '}'
    print output
    
