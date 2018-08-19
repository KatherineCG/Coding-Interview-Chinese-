class Solution:
    def SortInsert(self, a1, a2):
        if a1 == [] and a2 == []:
            return
        a1len = len(a1)
        a2len = len(a2)
        for i2 in range(a2len):
            for i1 in range(len(a1)):
                if a1[0] > a1[1]:
                    if a2[i2] >= a1[i1]:
                        a1.insert(i1, a2[i2])
                        break
                    if a2[i2] <= a1[len(a1)-1]:
                        a1.insert(len(a1), a2[i2])
                        break

                if a1[0] < a1[1]:
                    if a2[i2] <= a1[i1]:
                        a1.insert(i1, a2[i2])
                        break
                    if a2[i2] >= a1[len(a1)-1]:
                        a1.insert(len(a1), a2[i2])
                        break
        return a1

sortinsert = Solution()
a1 = raw_input()
a2 = raw_input()
array1 = a1.split()
array2 = a2.split()
print sortinsert.SortInsert(array1, array2)
