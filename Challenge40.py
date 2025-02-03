import random



def bubbleSort(myList):
    for passnum in range(len(myList)-1, 0, -1):
        for i in range(passnum):
            if myList[i] > myList[i+1]:
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp

myList = []

for i in range(10):
    myList.append(random.randint(0,100))               

print(myList)
bubbleSort(myList)
print(myList)
