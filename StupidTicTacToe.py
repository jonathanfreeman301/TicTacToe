#import pygame as p
import random 

game = int(input("Which game would you like to play? Type 1 to play tic tac toe with a computer. Type 2 to play tic tac toe with two players.Type 3 for hard mode (Computer goes first)\n"))
counter = 0
board = ['#','#','#','#','#','#','#','#','#']
rowWins = [[1,1,1,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1]]
colWins = [[1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1]]
diagWins = [[1,0,0,0,1,0,0,0,1],[0,0,1,0,1,0,1,0,0]]
wins = rowWins + colWins + diagWins

def showBoard():
        print(board[0]+"\t"+board[1]+"\t"+board[2]+"\n"+board[3]+"\t"+board[4]+"\t"+board[5]+"\n"+board[6]+"\t"+board[7]+"\t"+board[8])

def humanTicTacToe(counter):
    playing = True

    while(playing):
        showBoard()
        if counter % 2 == 0:
            userMove = int(input("Where would you like to place an X? "))
        else: 
            userMove = int(input("Where would you like to place an O? "))

        if board[userMove] == '#':
            if counter % 2 == 0:
                board[userMove] = 'x'
                if checkWin(board, 'x'):
                    showBoard()
                    print("X wins!")
                    break
            else:
                board[userMove] = 'o'
                if checkWin(board, 'o'):
                    showBoard()
                    print("O wins!")
                    break
            counter += 1       
        else: 
            print("Invalid move.")

        if tieChecker(counter):
                showBoard()
                break

def computerTicTacToe(counter):
        playing = True  

        while playing:
            showBoard()

            userMove = int(input("Where would you like to place an X? "))
            if board[userMove] == '#':
                board[userMove] = 'x'
                counter += 1
                if checkWin(board, 'x'):
                    showBoard()
                    print("X wins!")
                    playing = False
            else: 
                print("Invalid move.")

            counter = computerMove(board, counter)
            if checkWin(board, 'o'): 
                showBoard()
                print("The computer wins!")
                playing = False
            if tieChecker(counter):
                showBoard()
                playing = False

def hardModeTicTacToe(counter):
    playing = True  

    while playing:
        counter = computerMove(board, counter)
        if checkWin(board, 'o'): 
            showBoard()
            print("The computer wins!")
            break

        if tieChecker(counter):
            showBoard()
            break
        showBoard()
        userMove = int(input("Where would you like to place an X? "))
        if board[userMove] == '#':
            board[userMove] = 'x'
            counter += 1
            if checkWin(board, 'x'):
                showBoard()
                print("X wins!")
                break
        else: 
            print("Invalid move.")
        if tieChecker(counter):
            showBoard()
            break

def computerMove(board, counter):
     choosing = True
     while choosing:
        if computerWin():
            break
        elif computerBlock():
            counter += 1
            break
        else:
            availableMoves = [i for i, spot in enumerate(board) if spot == '#']
            if availableMoves:
                compMove = random.choice(availableMoves)
                board[compMove] = 'o'
                counter += 1
                break
     return counter

def checkWin(board, player):
     for win in wins:
         count = 0
         for i in range(9):
             if win[i] == 1 and board[i] == player:
                 count += 1
         if count == 3:
             return True
         
def computerBlock():
    for win in wins:
        count = 0
        for i in range(9):
            if win[i] == 1 and board[i] == 'x':
                count += 1
            if count == 2:
                for j in range(9):
                    if win[j] == 1 and board[j] == '#':
                        board[j] = 'o'
                        return True

def computerWin():
    for win in wins:
        count = 0
        for i in range(9):
            if win[i] == 1 and board[i] == 'o':
                count += 1
            if count == 2:
                for j in range(9):
                    if win[j] == 1 and board[j] == '#':
                        board[j] = 'o'
                        return True

def tieChecker(counter):
    if counter == 9:
        print("It's a tie!")
        return True
    else:
        return False
    
if game == 1:  
    computerTicTacToe(counter)

if game == 2:
    humanTicTacToe(counter)

if game == 3:
    hardModeTicTacToe(counter)