class Solution():
    def Fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fib(n - 1) + self.Fib(n - 2)
    
    def Fib1(self, n):
        fib = []
        fib.append(0)
        fib.append(1)
        '''
        if n == 0 or n == 1:
            return fib[n]
        '''
        for i in range(2, n + 1):
            fibi = fib[i-1] + fib[i-2]
            fib.append(fibi)
        return fib[n]
if __name__ == '__main__':
    test = Solution()
    #print test.Fib(1000)
    print ('***')
    print test.Fib1(1000)