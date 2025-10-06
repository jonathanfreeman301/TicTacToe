import pygame as p
import random 

p.init()
p.mixer.init()
screen = p.display.set_mode((1280, 720))
p.display.set_caption("Helldivers Tic Tac Toe")
screen.fill((135, 206, 235))
playing = True

victorySounds = []
Helldiver = p.image.load("assets/Helldiver.png").convert_alpha()
Hulk = p.image.load("assets/Hulk.png").convert_alpha()
victorySounds.append(p.mixer.Sound("assets/Democracy Officer - Victory was never in doubt.mp3"))
victorySounds.append(p.mixer.Sound("assets/Democracy Officer - Democracy prevails once more.mp3"))
victorySounds.append(p.mixer.Sound("assets/Democracy Officer - You have maintained our way of life.mp3"))
defeat = p.mixer.Sound("assets/Democracy officer - Our heroes have fallen.mp3")
tie = p.mixer.Sound("assets/Democracy officer - This operation is no longer viable.mp3")
ready = p.mixer.Sound("assets/Democracy Officer - Ready for another mission, helldiver.mp3")
music = p.mixer.music.load("assets/GalacticWar.mp3")
p.mixer.music.set_volume(0.1)
p.mixer.music.play(-1)

def drawGrid():
    screen.fill((135, 206, 235))
    screen.blit(text, text_rect)
    screen.blit(game1text, (180, 60))
    p.draw.line(screen, (255, 255, 255), [340, 300], [940, 300], 5)
    p.draw.line(screen, (255, 255, 255), [340, 500], [940, 500], 5)
    p.draw.line(screen, (255, 255, 255), [540, 100], [540, 700], 5)
    p.draw.line(screen, (255, 255, 255), [740, 100], [740, 700], 5)
    if checkWin('x'):
        screen.blit(wintext, wintext_rect)
    if checkWin('o'):
        screen.blit(defeattext, wintext_rect)
    if tieChecker(counter):
        screen.blit(tietext, tietext_rect)

font = p.font.SysFont('Comic Sans', 30)
text = font.render('Welcome to Helldivers Tic Tac Toe!', True, (255, 255, 255))
text_rect = text.get_rect(center=(640, 50))

font = p.font.SysFont('Comic Sans', 15)
game1text = font.render('Press R to Reset!', True, (255, 255, 255))
game1text_rect = game1text.get_rect(center=(250, 80))

winfont = p.font.SysFont('Comic Sans', 30)
wintext = font.render('The automatons have felt the full might of Democracy! Well done Helldiver!', True, (0, 0, 0))
wintext_rect = wintext.get_rect(center=(640, 80))

winfont = p.font.SysFont('Comic Sans', 30)
defeattext = font.render('This battle is lost. The fate of Democracy needs to be defended!', True, (0, 0, 0))
wintext_rect = wintext.get_rect(center=(640, 80))

tiefont = p.font.SysFont('Comic Sans', 30)
tietext = font.render('We are at a stalemate, Helldiver! We must prepare for redeployment.', True, (0, 0, 0))
tietext_rect = tietext.get_rect(center=(640, 80))

counter = 0
board = ['#','#','#','#','#','#','#','#','#']
rowWins = [[1,1,1,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1]]
colWins = [[1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1]]
diagWins = [[1,0,0,0,1,0,0,0,1],[0,0,1,0,1,0,1,0,0]]
wins = rowWins + colWins + diagWins

def drawBoard():
    for i, cell in enumerate(board):   
        r, c = divmod(i, 3)  
        center_x = 340 + c * 200 + 100
        center_y = 100 + r * 200 + 100

        if cell == 'x':
            img_rect = Helldiver.get_rect(center=(center_x, center_y))
            screen.blit(Helldiver, img_rect)
        elif cell == 'o':
            img_rect = Hulk.get_rect(center=(center_x, center_y))
            screen.blit(Hulk, img_rect)


def checkWin(player):
     for win in wins:
         count = 0
         for i in range(9):
             if win[i] == 1 and board[i] == player:
                 count += 1
         if count == 3:
             return True
     
def computerMove(counter):
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
                return compMove
         
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
        return True
    else:
        return False

#this is my shame..
def getCell(mouse_pos):
    x, y = mouse_pos
    if 340 <= x <= 940 and 100 <= y <= 700:
        if 340 <= x <= 540 and 100 <= y < 300:
            return 0
        elif 540 <= x < 740 and 100 <= y < 300:
            return 1
        elif 740 <= x <= 940 and 100 <= y < 300:
            return 2
        elif 340 <= x < 540 and 300 <= y < 500:
            return 3
        elif 540 <= x <= 740 and 300 <= y < 500:
            return 4
        elif 740 <= x < 940 and 300 <= y < 500:
            return 5
        elif 340 <= x <= 540 and 500 <= y < 700:
            return 6
        elif 540 <= x < 740 and 500 <= y < 700:
            return 7
        elif 740 <= x <= 940 and 500 <= y < 700:
            return 8
    else:
        return 9

turn = 'x'
while playing:
        #music.set_volume(0.1)
        mouse = p.mouse.get_pos()
        for event in p.event.get():
            if event.type == p.QUIT or p.key.get_pressed()[p.K_ESCAPE]:
                playing = False
            if event.type == p.KEYDOWN and p.key.get_pressed()[p.K_r]:
                #victory.stop()
                defeat.stop()
                tie.stop()
                board = ['#','#','#','#','#','#','#','#','#']
                counter = 0
                turn = 'x'
                ready.play()
                ready.set_volume(0.5)
            if event.type == p.MOUSEBUTTONDOWN and turn == 'x':
                cell = getCell(mouse)
                if cell != 9 and board[cell] == '#':
                    board[cell] = 'x' 
                    counter += 1
                    if checkWin('x'):
                        victory = random.choice(victorySounds)
                        victory.play()
                        victory.set_volume(0.5)
                        turn = None
                    elif tieChecker(counter):
                        tie.play()
                        tie.set_volume(0.4)
                        turn = None
                    else:
                        turn = 'o'
        
            if playing and turn == 'o':
                computerMove(counter)
                counter += 1
                if checkWin('o'):
                    defeat.play()
                    defeat.set_volume(0.6)
                    turn = None
                elif tieChecker(counter):
                    tie.play()
                    tie.set_volume(0.4)
                    turn = None
                else:
                    turn = 'x'
                    
        drawGrid()
        drawBoard()
        p.display.update()    

p.quit()