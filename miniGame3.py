# -*- coding: utf-8 -*-

import os, sys, random ,time , Module, Variable
import pygame as pg
import KingOfBet_LostInPokemonWorld,miniGame,database

def miniGame3(ID,playerName,Money,playedTimes=0,controlValue=0):
    falseTimes=0
    move=0
    Variable.FPSCLOCK = pg.time.Clock()
    # Tạo ảnh pokemon
    goldBoard_image,goldBoard_rect=Module.load_image("goldBoard.png","logIn")
    goldBoard_rect.center=(1180,50)
    wind_image,wind_rect=Module.load_image('wind.png',"miniGame3")
    fire_image,fire_rect=Module.load_image('fire.png',"miniGame3")
    bug_image,bug_rect=Module.load_image('bug.png',"miniGame3")
    eye_image,eye_rect=Module.load_image('eye.png',"miniGame3")
    earth_image,earth_rect=Module.load_image('earth.png',"miniGame3")
    BG_minigame3_image,BG_minigame3_rect=Module.load_image('background.png',"miniGame3")
    start3_image,start3_rect=Module.load_image('start.png',"miniGame3")
    return3_image,return3_rect=Module.load_image('quit.png',"miniGame3")
    retry3_image,retry3_rect=Module.load_image("retry.png","miniGame3")
    move_image,move_rect=Module.load_image('moves.png',"miniGame3")
    move_rect.center=(1200,300)
    ALLPICTURES = [wind_image, fire_image, eye_image,bug_image,earth_image]
    help_image,help_rect=Module.load_image("help.png","miniGame1")
    instruction_image,instruction_rect=Module.load_image("instruction.png","miniGame1")
    instruction_rect.center=(480,400)
    xButton_image,xButton_rect=Module.load_image("xButton.png","miniGame1")
    xButton_rect.center=(900,125)
    pg.display.set_caption('Memory Game')
    # Prepare Game Objects (tạo các vật thể trong game)
    clock = pg.time.Clock()
        # 1. Tạo nút bắt đầu:
    BG_minigame3_image.blit(start3_image,(1125,500))
    start3_rect=pg.Rect(1125,500,start3_rect.width,start3_rect.height)
        # 2. Tạo nút chơi lại:
    BG_minigame3_image.blit(retry3_image,(1150,600))
    retry3_rect=pg.Rect(1150,600,retry3_rect.width,retry3_rect.height)
        # 3. Tạo nút trở lại:
    BG_minigame3_image.blit(return3_image,(1150,675))
    return3_rect=pg.Rect(1200,675,return3_rect.width,return3_rect.height)
    revealedBoxes = generateRevealedBoxesData(False)
    firstSelection = None # stores the (x, y) of the first box clicked.
    mainBoard = getRandomizedBoard(ALLPICTURES)
    KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame3_image, (0, 0))
    if playedTimes==0:
        Module.printing("JosefinSans-BoldItalic.ttf",34,instruction_image,Variable.nenSangFont,'Do you want to see all elements in the pokemon world?',(530,100))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'In this game you will see them all!',(530,185))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'Each card hide a random element.',(530,225))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You will need to find two similar elements among them.',(530,265))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'Every wrong match will cost you 1 gold.',(530,305))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'But if you win, you will receive a huge return!!! ',(530,345))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You will win after all the matching elements were revealed.',(530,425))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You can play again by clicking "Retry".',(530,480))
        Module.printing("JosefinSans-BoldItalic.ttf",40,instruction_image,Variable.nenSangFont,'Power of Water, Power of Light! Powers Unite!!!',(530,530))
        KingOfBet_LostInPokemonWorld.screen.blit(instruction_image, instruction_rect)
        KingOfBet_LostInPokemonWorld.screen.blit(xButton_image,xButton_rect)
        pg.display.flip() 
        watchingTime=True
        while watchingTime:
            for event in pg.event.get():
                if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONUP: # Nếu chuột được nhấn và đã xóa hình ảnh
                    if pg.mouse.get_pressed:
                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                        x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                        if xButton_rect.collidepoint(x_mouse,y_mouse): #cái này bắt đầu chơi   
                            if playedTimes==0:
                                playedTimes=1
                                watchingTime=False
                            else:
                                controlValue=0
                                watchingTime=False
    help_rect.center=(1300,230)
    BG_minigame3_image.blit(help_image,help_rect)
    KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame3_image, (0, 0))
    pg.display.flip() 
    while True: # main game loop
        mouseClicked = False
        KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame3_image,(0,0))
        if controlValue==1:
            KingOfBet_LostInPokemonWorld.screen.blit(move_image,move_rect)
            Module.printing("JosefinSans-BoldItalic.ttf",40,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,f'{move}',move_rect.center)
        drawBoard(mainBoard, revealedBoxes)
        for event in pg.event.get(): # event handling loop
            if event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEMOTION:
                Variable.mousex, Variable.mousey = event.pos
            elif event.type == pg.MOUSEBUTTONUP:
                Variable.mousex, Variable.mousey = event.pos
                mouseClicked = True
            if event.type == pg.MOUSEBUTTONUP: # Nếu chuột được nhấn và đã xóa hình ảnh
                if pg.mouse.get_pressed :
                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                    if return3_rect.collidepoint(x_mouse,y_mouse): # cái này là thoát game
                        KingOfBet_LostInPokemonWorld.channel2.fadeout(1000)
                        KingOfBet_LostInPokemonWorld.channel1.set_volume(1)
                        KingOfBet_LostInPokemonWorld.channel1.play(KingOfBet_LostInPokemonWorld.nhapTen, -1)
                        miniGame.minigame(ID,playerName,Money)
                    if start3_rect.collidepoint(x_mouse,y_mouse) and controlValue==0: #Bắt đầu game
                        controlValue+=1
                    if retry3_rect.collidepoint(x_mouse,y_mouse): # chơi lại
                        miniGame3(ID,playerName,Money,1,1)
                    if help_rect.collidepoint(x_mouse,y_mouse):
                        if playedTimes>0:
                            Module.printing("JosefinSans-BoldItalic.ttf",34,instruction_image,Variable.nenSangFont,'Do you want to see all elements in the pokemon world?',(530,100))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'In this game you will see them all!',(530,185))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'Each card hide a random element.',(530,225))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You will need to find two similar elements among them.',(530,265))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'Every wrong match will cost you 1 gold.',(530,305))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'But if you win, you will receive a huge return!!! ',(530,345))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You will win after all the matching elements were revealed.',(530,425))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You can play again by clicking "Retry".',(530,480))
                            Module.printing("JosefinSans-BoldItalic.ttf",40,instruction_image,Variable.nenSangFont,'Power of Water, Power of Light! Powers Unite!!!',(530,530))
                        KingOfBet_LostInPokemonWorld.screen.blit(instruction_image, instruction_rect)
                        KingOfBet_LostInPokemonWorld.screen.blit(xButton_image,xButton_rect)
                        pg.display.flip() 
                        watchingTime=True
                        while watchingTime:
                            for event in pg.event.get():
                                if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                    pg.display.quit()
                                    pg.quit()
                                    sys.exit()
                                if event.type == pg.MOUSEBUTTONUP: # Nếu chuột được nhấn và đã xóa hình ảnh
                                    if pg.mouse.get_pressed:
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                        x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                                        if xButton_rect.collidepoint(x_mouse,y_mouse): #cái này bắt đầu chơi   
                                            if playedTimes==0:
                                                playedTimes=1
                                                watchingTime=False
                                                KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame3_image, (0, 0))
                                                pg.display.flip() 
                                            else:
                                                controlValue=0
                                                watchingTime=False
                                                KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame3_image, (0, 0))
                                                pg.display.flip() 
        # quá trình chơi game
        boxx, boxy = getBoxAtPixel(Variable.mousex, Variable.mousey)
        if boxx != None and boxy != None and controlValue==1:
            # The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxes(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # set the box as "revealed"
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                    move+=1
                else: # the current box was the second box clicked
                    # Check if there is a match between the two icons.
                    picture1 = getPicture(mainBoard, firstSelection[0], firstSelection[1])
                    picture2 = getPicture(mainBoard, boxx, boxy)
                    if picture1 != picture2:# chọn sai
                        # Icons don't match. Re-cover up both selections.
                        pg.time.wait(1000) # 1000 milliseconds = 1 sec
                        falseTimes+=1
                        coverBoxes(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): # cái này là thắng rồi
                        Money=Money+10-falseTimes
                        Variable.playerMoneys[ID-1]=Money
                        Module.printing("JosefinSans-BoldItalic.ttf",20,BG_minigame3_image,Variable.nenToiFont,'You win the game!!!',(1200,350))
                        Module.writeData(ID)
                        controlValue+=1
                        # Show the fully revealed board
                        drawBoard(mainBoard, revealedBoxes)
                        pg.display.update()
                    firstSelection = None
        # Redraw the screen and wait a clock tick.
        KingOfBet_LostInPokemonWorld.screen.blit(goldBoard_image,goldBoard_rect)
        Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,str(Money),(1150,50))
        pg.display.update()
        Variable.FPSCLOCK.tick(30)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(Variable.BOARDWIDTH):
        revealedBoxes.append([val] * Variable.BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard(ALLPICTURES):
    # Get a list of every possible shape in every possible color.
    numPicturesUsed = int(Variable.BOARDWIDTH * Variable.BOARDHEIGHT / 2) # calculate how many icons are needed
    random.shuffle(ALLPICTURES)
    pictures = ALLPICTURES[:numPicturesUsed] * 2 # make two of each
    random.shuffle(pictures)
    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(Variable.BOARDWIDTH):
        column = []
        for y in range(Variable.BOARDHEIGHT):
            column.append(pictures[0])
            del pictures[0] # remove the icons as we assign them
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (Variable.BOXWIDTH + Variable.GAPSIZE) + Variable.XMARGIN
    top = boxy * (Variable.BOXHEIGHT + Variable.GAPSIZE) + Variable.YMARGIN
    return (left, top)

def getBoxAtPixel(x, y):
    for boxx in range(Variable.BOARDWIDTH):
        for boxy in range(Variable.BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pg.Rect(left, top, Variable.BOXWIDTH, Variable.BOXHEIGHT)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def drawPicture(picture, boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    left=left+45
    top=top+80
    # Draw the picture
    KingOfBet_LostInPokemonWorld.screen.blit(picture, (left , top))

def getPicture(board, boxx, boxy):
    # picture value for x, y spot is stored in board[x][y]
    return board[boxx][boxy]

def drawBoxCovers(board, boxes,type):
    back_image,back_rect=Module.load_image('back.png',"miniGame3")
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        picture = getPicture(board, box[0], box[1])
        drawPicture(picture, box[0], box[1])
        if type=='cover': # only draw the cover if there is an coverage
            KingOfBet_LostInPokemonWorld.screen.blit(back_image, (left, top))     
    pg.display.update()

def revealBoxes(board, boxesToReveal):
    # Do the "box reveal" animation.
    type='reveal'
    drawBoxCovers(board, boxesToReveal,type)

def coverBoxes(board, boxesToCover):
    # Do the "box cover" animation.
    type='cover'
    drawBoxCovers(board, boxesToCover,type)


def drawBoard(board, revealed):
    back_image,back_rect=Module.load_image('back.png',"miniGame3")
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(Variable.BOARDWIDTH):
        for boxy in range(Variable.BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                KingOfBet_LostInPokemonWorld.screen.blit(back_image, (left, top))
            else:
                # Draw the (revealed) picture.
                picture = getPicture(board, boxx, boxy)
                drawPicture(picture, boxx, boxy)

def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pg.draw.rect(KingOfBet_LostInPokemonWorld.screen, Variable.BLUE, (left - 4, top - 4, Variable.BOXWIDTH + 4, Variable.BOXHEIGHT + 4), 4)

def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            return False # return False if any boxes are covered.
    return True