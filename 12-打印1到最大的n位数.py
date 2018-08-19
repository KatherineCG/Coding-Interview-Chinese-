class Solution():
    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            print 'Input Error'
            return
        else:
            string = ["0" for i in range(n)]
            self.Print1ToMaxOfNDigitsRecursively(string, n, 0)
    
    def Print1ToMaxOfNDigitsRecursively(self, string, length, start):
        if length == start:
            output = self.RemoveLeadingZeros("".join(string))
            if output != '0':
                print (output)
            return
        for i in range(0, 10):
            string[start] = repr(i)
            self.Print1ToMaxOfNDigitsRecursively(string, length, start+1)
    
    def RemoveLeadingZeros(self, string):
        i = 0
        for ch in string[:-1]:
            if ch == '0':
                i += 1
            else:
                break
        return string[i:]
            
test = Solution()
test.Print1ToMaxOfNDigits(0)
test.Print1ToMaxOfNDigits(2)