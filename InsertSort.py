def insertionSort(aList):
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp
myList = [14, 46, 43, 27, 57, 41, 45, 21, 70]
insertionSort(myList)
print(myList)
