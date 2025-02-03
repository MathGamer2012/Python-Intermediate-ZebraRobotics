import random 

def insertionSort(aList):
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp



myList = []

for i in range (10):
    myList.append(random.randint(0,100))
    
print(myList)
insertionSort(myList)
print(myList)
