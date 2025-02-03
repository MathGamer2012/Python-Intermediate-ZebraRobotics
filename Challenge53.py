theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
            
def drawBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])



def game():
    print("Welcome to Tic Tac Toe!") 
    player1 = input("Type O or X for your game symbol: ")
    player2 = ""
    question = "" 

    if player1 == "X":
        player2 = "O"

    else:
        player2 = "X" 
        
    turn = player1

    drawBoard(theBoard)

    for i in range(9):
            question = str(input("Where would " + turn + " like to move: "))
            theBoard[question] = turn 
            drawBoard(theBoard)
            if turn == player1:
                turn = player2

            else:
                turn = player1

            if theBoard['7'] == "X" and theBoard['3'] == "X" and theBoard['5'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['7'] == "O" and theBoard['3'] == "O" and theBoard['5'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['7'] == "X" and theBoard['8'] == "X" and theBoard['9'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['7'] == "O" and theBoard['8'] == "O" and theBoard['9'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['1'] == "X" and theBoard['2'] == "X" and theBoard['3'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['1'] == "O" and theBoard['2'] == "O" and theBoard['3'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['4'] == "X" and theBoard['5'] == "X" and theBoard['6'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['4'] == "O" and theBoard['5'] == "O" and theBoard['6'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['9'] == "X" and theBoard['5'] == "X" and theBoard['1'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['9'] == "O" and theBoard['5'] == "O" and theBoard['1'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['1'] == "X" and theBoard['4'] == "X" and theBoard['7'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['1'] == "O" and theBoard['4'] == "O" and theBoard['7'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['2'] == "X" and theBoard['5'] == "X" and theBoard['8'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['2'] == "O" and theBoard['5'] == "O" and theBoard['8'] == "O":
                print("Nice",player2, "you won!!!")
                break

            if theBoard['3'] == "X" and theBoard['6'] == "X" and theBoard['9'] == "X":
                print("Nice",player1, "you won!!!")
                break

            if theBoard['3'] == "O" and theBoard['6'] == "O" and theBoard['9'] == "O":
                print("Nice",player2, "you won!!!")
                break



game()

print("GG's It was a Draw")
question2 = str(input("Type Y if you want to play again, othewise type N: "))

if question2 == "Y" or "y":
    game()

if question2 == "N" or "n":
    print("Thanks for playing!!") 

    

         



