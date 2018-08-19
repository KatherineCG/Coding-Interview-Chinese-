class Solution():
    def doublePower(self, base, exponent):
        if base == 0 and exponent == 0:
            return 0
        elif exponent == 0:
            return 1
        elif exponent < 0:
            exponent = 0 - exponent
            power = self.Positive_doublePower(base, exponent)
            power = 1.0/power
        else:
            power = self.Positive_doublePower(base, exponent)
        return power
    
    def Positive_doublePower(self, base, exponent):
        power = base
        for i in range(2, exponent + 1):
            power = power * base
        return power

test = Solution()
print test.doublePower(10, -5)