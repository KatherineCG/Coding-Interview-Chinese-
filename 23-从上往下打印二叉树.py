#coding=utf-8
import Queue
import re
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        q = Queue.Queue()
        result = []
        if root != None:
            q.put(root)
        while not q.empty():
            node = q.get(0)
            result.append(node.val)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
        return result

def HandleInput(array):
    array = re.sub('[{}]', '', array).split(',')
    pRoot = None
    pRoot = CreateBinaryTree(array, pRoot)
    return pRoot
def CreateBinaryTree(data, root):
    if len(data) > 0:
        if data[0] == '#':
            return None
        else:
            root = TreeNode(data[0])
            data.pop(0)
            root.left = CreateBinaryTree(data, root.left)
            if len(data) > 0:
                data.pop(0)
                root.right = CreateBinaryTree(data, root.right)
            return root
    else:
        return None
test = Solution()
input = raw_input()
if input == '{}':
    root = None
else:
    root = HandleInput(input)
result = test.PrintFromTopToBottom(root)
if result == []:
    output = '[]'
else:
    output = ','.join(result)
    output = '[' + output + ']'
print output