def bubbleSort(myList):
    for passnum in range(len(myList)-1, 0, -1):
        for i in range(passnum):
            if myList[i] > myList[i+1]:
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp
myList = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubbleSort(myList)
print(myList)
