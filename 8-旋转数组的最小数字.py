class Solution():
    def Min(self, list):
        length = len(list)
        index1 = 0
        index2 = length - 1
        indexMid = index1
        while list[index1] >= list[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            indexMid = (index2 + index1) / 2
            if list[index2] == list[index1] and list[indexMid] == list[index1]:
                return self.MinInOrder(list, index1, index2)
            if list[indexMid] >=  list[index1]:
                index1 = indexMid
            elif list[indexMid] <= list[index2]:
                index2 = indexMid
        result = list[indexMid]
        return result
    def MinInOrder(self, list, index1, index2):
        result = list[index1]
        for index1 in range(1, index2):
            if list[index1] < result:
                result = list[index1]
        return result

if __name__ == '__main__':
    test = Solution()
    list1 = [1,0,1,1,1]
    list2 = [1,2,3,4,5]
    list3 = [3,4,5,1,2]
    print test.Min(list1)
    print test.Min(list2)
    print test.Min(list3)