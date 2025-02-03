import shelve

myFile = shelve.open("cuisine.dat", "n")
myFile["Chinese"] = ["Dumplings", "Fried noodles", "Peking duck"]
myFile["Indian"] = ["Shai Panner", "Naan", "Cholay"]
myFile["Mexican"] = ["Salsa", "Toco", "Burrito"]
myFile.sync()
print(myFile["Chinese"])
print(myFile["Indian"])
print(myFile["Mexican"])
