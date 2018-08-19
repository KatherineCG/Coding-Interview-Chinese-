# -*- coding:utf-8 -*-
import re
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        route = []
        currentsum = 0
        if root == None:
            return result
        result = self.Path(root, expectNumber, route, currentsum, result)
        return result
    def Path(self, root, expectNumber, route, currentsum, result):
        currentsum += root.val
        route.append(root)
        #如果是叶子结点，存入result
        isleaf = (root.left == None and root.right == None)
        if currentsum == expectNumber and isleaf:
            onepath = []
            for node in route:
                onepath.append(node.val)
            result.append(onepath)
        #如果不是叶子结点，则遍历它的子结点
        if root.left != None:
            self.Path(root.left, expectNumber, route, currentsum, result)
        if root.right != None:
            self.Path(root.right, expectNumber, route, currentsum, result)
        #在返回到父结点之前，在路径上删除当前结点，并在currentsum中减去当前结点的值
        currentsum -= root.val
        route.pop()
        return result
def handleinput(array):
    array = re.sub('[{}]', '', array).split(',')
    pRoot = CreateBinaryTree(array,0)
    return pRoot
def CreateBinaryTree(data,n):
    if len(data) > 0:
        if n < len(data):
            if data[n] != '#':
                root = TreeNode(int(data[n]))
                if n+2 < len(data) and data[n+1] == '#' and data[n+2] != '#':
                    if (n+3 < len(data) and data[n+3] == '#') or n+3 == len(data):
                        l = n+2
                        r = n+3
                else:
                    l = 2*n+1
                    r = 2*n+2
                root.left = CreateBinaryTree(data,l)
                root.right = CreateBinaryTree(data,r)
                return root
            else:
                return None
        else:
            return None
    else:
        return None
test = Solution()
inputarray = raw_input()
for i in range(len(inputarray)-1,0,-1):
    if inputarray[i] == ',':
        break
expectNumber = int(inputarray[i+1:])
handlearray = inputarray[0:i]
result = []
if handlearray == '{}':
    print result
else:
    pRoot = handleinput(handlearray)
    result = test.FindPath(pRoot, expectNumber)
    if result == []:
        print '[]'
    else:
        output = ''
        for ch in result:
            ch = map(str, ch)
            ch = ','.join(ch)
            ch = '[' + ch + ']'
            output += ch + ','
        output = '[' + output[:len(output)-1] + ']'
        print output