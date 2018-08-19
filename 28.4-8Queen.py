# coding=utf-8
import random
class Solution():
    def conflict(self, state, nextx):
        #'定义冲突函数,state为元组，nextx为下一个皇后的水平位置即纵坐标，nexty为下一个皇后的垂直位置即横坐标'
        nexty = len(state)#通过state的长度，限制了每次都不在同一行
        for i in range(nexty):
            if abs(state[i] - nextx) in (0, nexty - i):
                # 若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突。
                # 如果abs(state[i] - nextx)=0，则表示在同一列，如果abs(state[i] - nextx)=nexty-1，则表示在对角线上
                #对角线两点：横坐标之差等于纵坐标之差
                return True
        return False

    def queens(self, num=8, state=()):
        #'八皇后问题，这里num表示规模'
        for pos in range(num):
            if not self.conflict(state, pos):  # 位置不冲突
                if len(state) == num - 1:  # 若是最后一个皇后，则返回该位置
                    yield (pos+1,)
                else:  # 若不是最后一个皇后，则将该位置返回到state元组并传给后面的皇后
                    for result in self.queens(num, state + (pos,)):
                        yield (pos+1,) + result

    def prettyp(self, solution):
        #'打印函数'
    
        def line(pos, length=len(solution)):
            #'打印一行，皇后位置用X填充，其余用0填充'
            return 'O' * (pos) + 'X' + 'O' * (length - pos - 1)
    
        for pos in solution:
            print(line(pos))
test = Solution()
result = list(test.queens(8))
b = input()
output = ''
for ch in result[b-1]:
    output += repr(ch)
print output
#prettyp(random.choice(list(queens(8))))