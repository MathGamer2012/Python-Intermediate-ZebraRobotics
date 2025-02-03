def selectionSort(myList):
    for i in range(len(myList)):
        least = i
        for k in range(i+1, len(myList)):
            if myList[k] < myList[least]:
                least = k
        temp = myList[least]
        myList[least] = myList[i]
        myList[i] = temp
myList = [14, 46, 43, 27, 57, 41, 45, 21, 70]
selectionSort(myList)
print(myList)
    
        
