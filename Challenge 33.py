smartFile = open("Challenge33.txt", "r")
question = str(input(smartFile.readline()+ "Write your answer here:"))
word =  smartFile.readline(40).rstrip('\n')
question = question.lower()

if question == word:
    print("Correct Answer")
else:
    print("Nice Try but it is wrong")

smartFile.close()
