# coding=utf-8
class Solution():
    global g_maxValue
    g_maxValue = 6
    def NumberOfNDice(self, n, s):
        if n < 1:
            return
        maxsum = n * g_maxValue
        pProbalities = [0 for i in range(n, maxsum+1)]
        self.Probability1(n, pProbalities)
        total = pow(g_maxValue, n)
        for i in range(n, maxsum+1):
            ratio = format(float(pProbalities[i-n])/float(total),'.2f')
            print ratio
        return
    def Probability1(self, n, pProbabilities):
        #每次都是第一个骰子，i代表骰子当时的点数，为初始sum
        for i in range(1, g_maxValue+1):
            self.Probability(n, n, i, pProbabilities)
    def Probability(self, original, current, sum, pProbabilities):
        if current == 1:
            pProbabilities[sum - original] += 1
        else:
            #余下每个骰子，分别从点数从1开始循环
            for i in range(1, g_maxValue+1):
                self.Probability(original, current-1, i+sum, pProbabilities)
        
test = Solution()
test.NumberOfNDice(2,1)