import random

def bubbleSort(myList):
    for passnum in range(len(myList)-1, 0, -1):
        for i in range(passnum):
            if myList[i] > myList[i+1]:
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp

def linearSearch(item, myList):
    found = False
    position = 1
    while position < len(myList) and not found:
        if myList[position] == item:
            found = print("You placed number" , position , "in the marathon")
            return found
        position = position + 1
    
myList = []

for i in range(200):
    myList.append(random.randint(0,100))

time = int(input("Write your time for the marathons(minutes): "))
if time not in myList:
    myList.append(time)
    
bubbleSort(myList)
linearSearch(time, myList)
