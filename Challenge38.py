import shelve

menu = print("Choose a team to list its players: \n 1. Toronto Raptors \n 2. Boston Celt \n 3. Atlanta Hawks \n 4. Golden State Warriors \n 5. Sacramento Kings \n 6. Exit the system")
choice = int(input("Your Selection: "))

myFile = shelve.open("cuisine.dat", "n")
while choice != 6:
    
    if choice == 1:
        myFile["Raptors"] = ["OG Anunoby", "Chris Boucher", "Oshae Brissett","Terence Davis", "Marc Gasol",]
        myFile.sync()
        print(myFile["Raptors"])
        menu = print("Choose a team to list its players: \n 1. Toronto Raptors \n 2. Boston Celt \n 3. Atlanta Hawks \n 4. Golden State Warriors \n 5. Sacramento Kings \n 6. Exit the system")
        choice = int(input("Your Selection: "))
        

    if choice == 2:
        myFile["Boston"] = ["JAYLEN BROWN", "CARSEN EDWARDS", "TACKO FALL", "JAVONTE GREEN", "GORDON HAYWARD"]
        myFile.sync
        print(myFile["Boston"])
        menu = print("Choose a team to list its players: \n 1. Toronto Raptors \n 2. Boston Celt \n 3. Atlanta Hawks \n 4. Golden State Warriors \n 5. Sacramento Kings \n 6. Exit the system")
        choice = int(input("Your Selection: "))

    if choice == 3:
        myFile["Atlanta"] = ["DeAndre' Bembry", "Charlie Brown Jr","Clint Capela", "John Collins", "Dewayne Dedmon"]
        myFile.sync
        print(myFile["Atlantas"])
        menu = print("Choose a team to list its players: \n 1. Toronto Raptors \n 2. Boston Celt \n 3. Atlanta Hawks \n 4. Golden State Warriors \n 5. Sacramento Kings \n 6. Exit the system")
        choice = int(input("Your Selection: "))

    if choice == 4:
        myFile["GSW"] = ["Ky Bowman", "Marquese Chriss", "Stephen Curry", "Draymond Green","Damion Lee"]
        myFile.sync
        print(myFile["GSW"])
        menu = print("Choose a team to list its players: \n 1. Toronto Raptors \n 2. Boston Celt \n 3. Atlanta Hawks \n 4. Golden State Warriors \n 5. Sacramento Kings \n 6. Exit the system")
        choice = int(input("Your Selection: "))

    if choice == 5:
        myFile["Sacramento"] = ["Marvin Bagley III", "Harrison Barnes","Kent Bazemore","Nemanja Bjelica","Bogdan Bogdanovic"]
        myFile.sync
        print(myFile["Sacramento"])
        menu = print("Choose a team to list its players: \n 1. Toronto Raptors \n 2. Boston Celt \n 3. Atlanta Hawks \n 4. Golden State Warriors \n 5. Sacramento Kings \n 6. Exit the system")
        choice = int(input("Your Selection: "))

    if choice == 6:
        break
