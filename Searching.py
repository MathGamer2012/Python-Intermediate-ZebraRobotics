def linearSearch(item, myList):
    found = False
    position = 0

    while position < len(myList) and not found:
        if myList[position] == item:
            found = True
        position = position + 1
    return found 
