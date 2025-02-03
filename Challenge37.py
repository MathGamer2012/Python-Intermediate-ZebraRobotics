import shelve

myFile = shelve.open("cuisine.dat", "n")
myFile["Drama"] = ["Wonder", "Real Steel", "The Karate Kid"]
myFile["Action"] = ["Fast & Furious", "Avengers:Endgame", "Logan"]
myFile["Family"] = ["Big Hero 6", "Diary of the Wimpy kid", "The Croods"]
myFile.sync()

print(myFile["Action"])

