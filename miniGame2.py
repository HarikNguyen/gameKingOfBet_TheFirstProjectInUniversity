# -*- coding: utf-8 -*-

"""
    Công việc: Tạo một game đơn giản yêu cầu người chơi tìm ra một bức ảnh khác biết trong một đống bức ảnh giống nhau hoàn toàn.
    Đối tượng người dung: game thủ và sinh viên của lớp CTT4 - KHTN.
    Nền tảng: Hệ điều hành Windows.
    Môi trường sử dụng: Giao diện đồ họa người chơi.
    Các chức năng cần có: - Xuất ra màn hình một khung ảnh với một đống bức ảnh giống nhau với bức "imposter".
                          - Người chơi sử dụng chuột để chọn bức ảnh khác biệt.
                          - Kiểm tra bức ảnh người chơi chọn là đúng hay sai.
    Thử nghiệm & Tìm kiếm lỗi: - Số lượng ảnh từ ít đến nhiều.
                               - Kích cỡ của các bức ảnh từ lớn đến nhỏ.
    Người phát triên: facebook.com/topsiu1.ds
    Liên hệ:  topsiu1.ds@gmail.com
              or 20120509@gmail.com
"""

__version__= 0.0
__maintainer__ = "facebook.com/topsiu1.ds"
__status__= "Prototype"
__date__ = "2/12/2020"

import os, sys, random ,time , Module, Variable
import pygame as pg
import KingOfBet_LostInPokemonWorld,miniGame,database

def miniGame2(ID,playerName,Money,playedTimes=0,controlValue=0):
    """Hàm này được gọi khi người chơi muốn chơi minigame "Tìm kẻ mạo danh"
       This function will be called when the player want to play minigame "The imposter"."""
    # Khai báo biến nội bộ trong minigame 2:
    row=14
    colum=23
    square_size=32
    #Khởi tạo khung hình và những thứ cần thiết
    pg.display.set_caption("The Imposter!!")
    pg.mouse.set_visible(1)
    # Khởi tạo hình ảnh:
    goldBoard_image,goldBoard_rect=Module.load_image("goldBoard.png","logIn")
    goldBoard_rect.center=(1150,550)
    picture1A_image,picture1A_rect=Module.load_image("couple1A.png","miniGame2")
    picture1B_image,picture1B_rect=Module.load_image("couple1B.png","miniGame2")
    picture1C_image,picture1C_rect=Module.load_image("couple1C.png","miniGame2")
    BG_minigame2_image,BG_minigame2_rect = Module.load_image("background1.png","miniGame2")
    start2_image,start2_rect=Module.load_image('startbutton1.png',"miniGame2")
    playAgain2_image,playAgain2_rect=Module.load_image('retry.png',"miniGame2")
    return2_image,return2_rect=Module.load_image('quit.png',"miniGame2")
    clock2_image,clock2_rect=Module.load_image("clock.png","miniGame2")
    help_image,help_rect=Module.load_image("help.png","miniGame1")
    instruction_image,instruction_rect=Module.load_image("instruction.png","miniGame1")
    instruction_rect.center=(480,400)
    xButton_image,xButton_rect=Module.load_image("xButton.png","miniGame1")
    xButton_rect.center=(900,125)
        # Khởi tạo vị trí các bức ảnh và chọn vị trí "imposter":
    pictures=[] # Khai báo biến "danh sách"(list) (vị trị của các bức ảnh).
    pictures_xy=[] # vị trí tọa độ điểm đầu tiên của các tấm hình.
    for j in range(0,row):
        for i in range(0+j*colum,colum*(j+1)):
            pictures.append(pg.Rect(117+(i-j*colum)*(2.5+square_size),140+j*(3+square_size),square_size,square_size)) # Thêm vị trí của các hình vào list pictures.
            pictures_xy.append((117+(i-j*colum)*(2.5+square_size),140+j*(3+square_size)))# thêm tọa độ điểm đầu mỗi hình vào list pictures_xy.
    imposter=random.choice(pictures_xy) # chọn ra vị trí của imposter.  
        # Khởi tạo các bộ hình ảnh:
    characters=[picture1A_image,picture1B_image,picture1C_image]
    randomImposter=random.choice(characters)
    randomReal=random.choice(characters)
    while randomReal==randomImposter:
        randomReal=random.choice(characters)
    # Display The Background
    KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame2_image, (0, 0)) # in cái background mình tạo ở trên lên màn hình
    if playedTimes==0:
        Module.printing("JosefinSans-BoldItalic.ttf",45,instruction_image,Variable.nenSangFont,u'Can You Find "The Imposter" ???',(530,100))
        Module.printing("JosefinSans-BoldItalic.ttf",40,instruction_image,Variable.nenSangFont,'HOW TO PLAY?',(530,155))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'In this simple minigame, you will become a detective.',(530,185))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You will need to find "The Imposter" among other pokemons.',(530,225))  
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You have 5s after "start" the game to find it.',(530,265))
        Module.printing("JosefinSans-BoldItalic.ttf",27,instruction_image,Variable.nenSangFont,'If you found "The Imposter" you win the game and receive 5 gold. ',(530,305))   
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'And if you didn\'t, you lose.',(530,345))
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You can play again by clicking "Retry".',(530,390)) 
        Module.printing("JosefinSans-BoldItalic.ttf",38,instruction_image,Variable.nenSangFont,'An empire toppled by its enemies can rise again.',(530,490))    
        Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'But one which crumbles from within? That\'s dead... forever!!!',(530,550))
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
    # Prepare Game Objects (tạo các vật thể trong game)
        # 1. Tạo nút bắt đầu:
    BG_minigame2_image.blit(start2_image,(1050,600))
    start2_rect=pg.Rect(1050,600,start2_rect.width,start2_rect.height)
        # 2. Tạo nút chơi lại:
    BG_minigame2_image.blit(playAgain2_image,(950,675))
    playAgain2_rect=pg.Rect(950,675,playAgain2_rect.width,playAgain2_rect.height)
        # 4. Tạo nút trở lại:
    BG_minigame2_image.blit(return2_image,(1150,675))
    return2_rect=pg.Rect(1200,675,return2_rect.width,return2_rect.height)
        # 3. Tạo đồng hồ:
    clock2 = pg.time.Clock()
    timer = pg.USEREVENT + 1                                                
    pg.time.set_timer(timer, 1000)
    timer_font = pg.font.SysFont('JosefinSans-BoldItalic.ttf', 38)
    timer_sec = 6
    timer_text = timer_font.render("00:06", True, (255, 255, 255))
    help_rect.center=(1295,275)
    BG_minigame2_image.blit(help_image,help_rect)
    KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame2_image, (0, 0))
    pg.display.flip()  
    # # Main Loop ( vòng lặp chính nơi diễn ra các sự kiện và tương tác của người chơi)
    while True:
        clock2.tick(60)
        current_time=pg.time.get_ticks()
        # Hiện hình ảnh:
        if controlValue==1:
            for i in pictures_xy:
                if i!=imposter:
                    BG_minigame2_image.blit(randomReal,i)
                else:
                    BG_minigame2_image.blit(randomImposter,i)
            controlValue+=1
        # Bắt sự kiện:
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == timer and controlValue==2:    # checks for timer event
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = timer_font.render("00:%02d" % timer_sec, True, (255, 255, 0))
                    timer_textRect=timer_text.get_rect()
                    timer_textRect.center = (1120,290)
                    BG_minigame2_image.blit(clock2_image, (1050,265))
                    BG_minigame2_image.blit(timer_text, timer_textRect)
                else:# chỗ này là thua game
                    pg.time.set_timer(timer, 0)    # turns off timer event
                    Module.printing("JosefinSans-BoldItalic.ttf",20,BG_minigame2_image,Variable.nenToiFont,'The imposter run away!you lose!!!',(1150,350))
                    controlValue+=1
            if event.type == pg.MOUSEBUTTONUP: # Nếu chuột được nhấn và đã xóa hình ảnh
                if pg.mouse.get_pressed and controlValue==0:
                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                    if start2_rect.collidepoint(x_mouse,y_mouse): # cái này là bắt đầu chơi
                        controlValue+=1
                # Kiểm tra lựa chọn của người chơi
                if pg.mouse.get_pressed and controlValue==2:
                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                    for i in range(0,colum*row):  # kiểm tra ô nào được chọn
                        if  pictures[i].collidepoint(x_mouse,y_mouse):  # xác định vị trí của ô đó rồi lấy màu hiện tại ở ô đó
                            if pictures_xy[i]==imposter:# cái này là tìm ra imposter
                                Money=Money+5
                                Variable.playerMoneys[ID-1]=Money
                                Module.writeData(ID)
                                Module.printing("JosefinSans-BoldItalic.ttf",20,BG_minigame2_image,Variable.nenToiFont,'You had found the imposter!!!',(1150,350))
                                controlValue+=1
                if pg.mouse.get_pressed : # Nếu chuột được nhấn
                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                    if playAgain2_rect.collidepoint(x_mouse,y_mouse) and controlValue==3: # chơi lại
                        miniGame2(ID,playerName,Money,1,1)
                    if return2_rect.collidepoint(x_mouse,y_mouse): # thoát game
                        KingOfBet_LostInPokemonWorld.channel2.fadeout(1000)
                        KingOfBet_LostInPokemonWorld.channel1.set_volume(1)
                        KingOfBet_LostInPokemonWorld.channel1.play(KingOfBet_LostInPokemonWorld.nhapTen, -1)
                        miniGame.minigame(ID,playerName,Money)
                    if help_rect.collidepoint(x_mouse,y_mouse):
                        if playedTimes>0:
                            Module.printing("JosefinSans-BoldItalic.ttf",45,instruction_image,Variable.nenSangFont,u'Can You Find "The Imposter" ???',(530,100))
                            Module.printing("JosefinSans-BoldItalic.ttf",40,instruction_image,Variable.nenSangFont,'HOW TO PLAY?',(530,155))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'In this simple minigame, you will become a detective.',(530,185))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You will need to find "The Imposter" among other pokemons.',(530,225))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You have 5s after "start" the game to find it.',(530,265))
                            Module.printing("JosefinSans-BoldItalic.ttf",27,instruction_image,Variable.nenSangFont,'If you found "The Imposter" you win the game and receive 5 gold. ',(530,305))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'And if you didn\'t, you lose.',(530,345))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'You can play again by clicking "Retry".',(530,390))
                            Module.printing("JosefinSans-BoldItalic.ttf",38,instruction_image,Variable.nenSangFont,'An empire toppled by its enemies can rise again.',(530,490))
                            Module.printing("JosefinSans-BoldItalic.ttf",30,instruction_image,Variable.nenSangFont,'But one which crumbles from within? That\'s dead... forever!!!',(530,550))
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
                                                KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame2_image, (0, 0))
                                                pg.display.flip() 
                                            else:
                                                controlValue=0
                                                watchingTime=False
                                                KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame2_image, (0, 0))
                                                pg.display.flip() 
        # Draw Everything
        KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame2_image, (0, 0)) # in background ( câu lệnh này chưa hiểu để làm gì cho lắm ) nhưng mà thiếu thì chả có hình ảnh gì trên màn hình
        KingOfBet_LostInPokemonWorld.screen.blit(goldBoard_image,goldBoard_rect)
        Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,str(Money),(1120,550))
        pg.display.flip() # cập nhật màn hình

