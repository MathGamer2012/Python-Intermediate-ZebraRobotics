smartFile = open("Challenge34.txt", "r")
question = ""
question2 = ""
question3 = ""
score = 0 

question = str(input(smartFile.readline()+ "Write your answer here:"))
word =  smartFile.readline(40).rstrip('\n')
question = question.lower()

if question == word:
    print("Correct Answer")
    score += 1 
else:
    print("Nice Try but it is wrong")
    


question2 = str(input(smartFile.readline(60)+ "Write your answer here:"))
question2 = question2.lower()
word2 = smartFile.readline(95).rstrip('\n')

if question2 == word2:
    print("Correct Answer")
    score += 1
else:
    print("Nice Try but it is wrong")

question3 = str(input(smartFile.readline(110)+ "Write your answer here:"))
question3 = question3.lower()
word3 = smartFile.readline(150).rstrip('\n')

if question3 == word3:
    print("Correct Answer")
    score += 1
else:
    print("Nice Try but it is wrong")

print("You got", score, "out of 3")





smartFile.close()
