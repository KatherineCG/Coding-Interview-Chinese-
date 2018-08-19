class Solution():
    def PrintProbability(self, n):
        g_maxValue = 6
        if n < 1:
            return
        pProbabilities = [[], []]
        pProbabilities[0] = [0 for i in range(g_maxValue * n + 1)]
        pProbabilities[1] = [0 for i in range(g_maxValue * n + 1)]
        flag = 0
        for i in range(1, g_maxValue+1):
            pProbabilities[flag][i] = 1
        for k in range(2, n+1):
            for i in range(k):
                pProbabilities[1-flag][i] = 0
            for i in range(k, g_maxValue*k+1):
                pProbabilities[1-flag][i] = 0
                j = 1
                while j<=i and j<=g_maxValue:
                    pProbabilities[1-flag][i] += pProbabilities[flag][i-j]
                    j+=1
            flag = 1 - flag
        total = pow(g_maxValue, n)
        for i in range(n, g_maxValue*n + 1):
            ratio = format(float(pProbabilities[flag][i]) / float(total), '.2f')
            print ratio
        return
test = Solution()
test.PrintProbability(4)