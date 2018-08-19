class Solution():
    def jump(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.jump(n - 1) + self.jump(n - 2)
    
    def jump1(self, n):
        num = []
        num.append(1)
        num.append(2)
        if n == 1 or n == 2:
            return num[n]
        for i in range(2, n):
            numnow = num[i-1] + num[i-2]
            num.append(numnow)
        return num[n-1]
if __name__ == '__main__':
    test = Solution()
    print test.jump(3)
    print test.jump1(3)