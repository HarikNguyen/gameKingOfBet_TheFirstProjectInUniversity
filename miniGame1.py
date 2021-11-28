# -*- coding: utf-8 -*-

"""
    Công việc: Tạo một game đơn giản yêu cầu người chơi vẽ lại hình ảnh được đưa ra dưới dạng bảng tính.
    Đối tượng người dung: game thủ và sinh viên của lớp CTT4 - KHTN.
    Nền tảng: Hệ điều hành Windows.
    Môi trường sử dụng: Giao diện đồ họa người chơi.
    Các chức năng cần có: - Tạo ra và xuất ra màn hình một bức hình đơn giản dưới dạng bản tính.
                          - Người chơi có thể sử dụng chuột để chọn các ô tính từ đó vẻ lại bức ảnh đã được đưa ra.
                          - Nhận lại và đọc được bức ảnh do người chơi vừa mới vẽ.
    Thử nghiệm & Tìm kiếm lỗi: - Sử dụng các hình ảnh từ đơn giản đến phức tạp.
                               - Tốc độ của người chơi chọn các ô tính.
    Người phát triên: facebook.com/topsiu1.ds
    Liên hệ:  topsiu1.ds@gmail.com
              or 20120509@gmail.com
"""

__version__= 1.3
__maintainer__ = "facebook.com/topsiu1.ds"
__status__= "Close Beta"
__date__ = "11/12/2020"

import os, sys, random ,time , Module, Variable
import pygame as pg
import KingOfBet_LostInPokemonWorld,miniGame,database

def miniGame1(ID,playerName,Money,playedTimes=0,gameTime=0,controlValue=0):
    """ Hàm này được gọi khi người chơi muốn chơi mini game "Trí nhớ siêu phàm".
        This function is called when the program the player want to play mini game "The Mighty Brain"."""
    # Khai báo biến ( không biết sao khai báo ở ngoài hàm main thì k dùng được)
    default_color=(255, 219, 217)
    square_size=50
    random_color=random.choice(Variable.color)
    row=10
    colum=10
    numberOfSquares=15
    remember_time=16000
    right_squares=0
    selectCount=0
    wrong_squares=0
    nenNau=(74,67,50)
    nenNauRect=pg.Rect(987,225,389,350)
    countDownControl=1
    watchingTime=None
    # Khởi tạo hình ảnh:
    goldBoard_image,goldBoard_rect=Module.load_image("goldBoard.png","logIn")
    goldBoard_rect.center=(1180,550)
    BG_minigame1_image,BG_minigame1_rect = Module.load_image("background.png","miniGame1")
    yellowSquare_image,yellowSquare_rect=Module.load_image("yellowSquare.png","miniGame1")
    blackSquare_image,blackSquare_rect=Module.load_image("blackSquare.png","miniGame1")
    redSquare_image,redSquare_rect= Module.load_image("redSquare.png","miniGame1")    
    finishButton_image,finishButton_rect= Module.load_image('finishbutton.png',"miniGame1")
    startButton_image,startButton_rect= Module.load_image('startbutton.png',"miniGame1")
    playAgainButton_image,playAgainButton_rect= Module.load_image('retry.png',"miniGame1")
    quit1_image,quit1_rect=Module.load_image('quit.png',"miniGame1")
    clock_image,clock_rect=Module.load_image("clock.png","miniGame1")
    clock_rect.center=(1180,350)
    help_image,help_rect=Module.load_image("help.png","miniGame1")
    instruction_image,instruction_rect=Module.load_image("instruction.png","miniGame1")
    instruction_rect.center=(480,400)
    xButton_image,xButton_rect=Module.load_image("xButton.png","miniGame1")
    xButton_rect.center=(900,150)
        # Tạo khối màu:
    yellow_color=yellowSquare_image.get_at((25,25)) # set màu của khối cho một biến
    # tương tự ở trên đều với khối màu đen
    black_color=blackSquare_image.get_at((25,25))
    red_color=redSquare_image.get_at((25,25))
     # Khởi tạo vị trí các khối màu"
    squares=[] # Khai báo biến "danh sách"(list) (vị trị cua khối)
    squares_xy=[] # vị trí tọa độ điểm đầu tiên của khối
    for j in range(0,10):
        for i in range(0+j*10,j*10+10):
            squares.append(pg.Rect(225+(i-j*10)*(3+square_size),130+j*(3+square_size),square_size,square_size)) # Thêm vị trí của các khối vào list squares.
            squares_xy.append((225+(i%10)*(3+square_size),130+int(i/10)*(3+square_size)))# thêm tọa độ điểm đầu mỗi khối vào list squares_xy
    random_squares=random.sample(squares_xy,numberOfSquares) # chọn ra số lượng khối để vẽ màu( trong hình người chơi cần ghi nhớ)     
    # Display The Background
    KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame1_image, (0, 0)) # in cái background mình tạo ở trên lên màn hình
    pg.display.flip()  # cập nhật màn hình
    # Tạo hướng dẫn chơi:
    if playedTimes==0:
        Module.printing("JosefinSans-BoldItalic.ttf",40,instruction_image,Variable.nenSangFont,u'Welcome to "Super Memory"',(530,100))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'HOW TO PLAY?',(530,155))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Click "Start" and the game will start after 2s',(530,185))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Fifteen yellow squares will appear randomly.',(530,225))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Your job is to remember the position of them.',(530,265))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'After 15s they will disappear. ',(530,305))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'You need to use your memory to point out ',(530,345))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'all squares\' position.',(530,385))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'You have unlimited time to do it.',(530,425))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Click "End" to see the answer and get gold.',(530,465))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Each right position gives you 1000 gold.',(530,505))
        Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'You can play again by clicking "Retry".',(530,545))
        Module.printing("JosefinSans-BoldItalic.ttf",45,instruction_image,Variable.nenSangFont,'Shall we play a game?',(530,590))
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
    clock = pg.time.Clock()
        # 1.Nút finish 
    BG_minigame1_image.blit(finishButton_image,(1200,600))
    finishButton_rect=pg.Rect(1200,600,finishButton_rect.width,finishButton_rect.height)
        # 2. Tạo nút bắt đầu:
    BG_minigame1_image.blit(startButton_image,(1025,600))
    startButton_rect=pg.Rect(1025,600,startButton_rect.width,startButton_rect.height)
        # 3. Tạo nút chơi lại:
    BG_minigame1_image.blit(playAgainButton_image,(990,675))
    playAgainButton_rect=pg.Rect(990,675,playAgainButton_rect.width,playAgainButton_rect.height)
        # 4. Tạo nút out minigame:
    BG_minigame1_image.blit(quit1_image,(1180,675))
    quit1_rect=pg.Rect(1180,675,quit1_rect.width,quit1_rect.height)
        # 5. Tạo đồng hồ
    timer = pg.USEREVENT + 1                                                
    pg.time.set_timer(timer, 1000)
    timer_font = pg.font.SysFont('JosefinSans-BoldItalic.ttf', 38)
    timer_sec = 15
    timer_text = timer_font.render("00:15", True, (255, 255, 255))
        #help
    help_rect.center=(1300,290)
    BG_minigame1_image.blit(help_image,help_rect)
    KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame1_image, (0, 0))
    # Main Loop ( vòng lặp chính nơi diễn ra các sự kiện và tương tác của người chơi)
    pg.display.flip()  
    while True:
        clock.tick(60)
        current_time=pg.time.get_ticks()-gameTime
        # Hiện hình yêu cầu
        if current_time>2000 and controlValue==1:      # Kiểm tra thời gian ghi nhớ     
            for i in range(0,numberOfSquares):
                BG_minigame1_image.blit(yellowSquare_image,random_squares[i]) # in hình cần ghi nhớ
            pg.display.flip()
            controlValue+=1
        # Xóa hình yêu cầu
        if current_time>remember_time+2000 and controlValue==2: #kiểm tra thời gian ghi nhớ
            for i in range(0,numberOfSquares):
                BG_minigame1_image.blit(blackSquare_image,random_squares[i]) # xóa hình ghi nhớ
            pg.display.flip()
            controlValue+=1
        # Bắt sự kiện:
        for event in pg.event.get():
            #điều khiển thời gian
            if event.type == timer and controlValue==2:    # checks for timer event
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = timer_font.render("00:%02d" % timer_sec, True, (255, 255, 0))
                    timer_textRect=timer_text.get_rect()
                    timer_textRect.center = (1180,350)
                    BG_minigame1_image.blit(clock_image, clock_rect)
                    BG_minigame1_image.blit(timer_text, timer_textRect)
                else:
                    pg.draw.rect(BG_minigame1_image,nenNau,nenNauRect)
                    pg.time.set_timer(timer, 0)    # turns off timer event
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP: # Nếu chuột được nhấn và đã xóa hình ảnh
                if pg.mouse.get_pressed:
                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                    if   controlValue==0:
                        if startButton_rect.collidepoint(x_mouse,y_mouse): #cái này bắt đầu chơi   
                            controlValue+=1
                            gameTime=pg.time.get_ticks()
                    if help_rect.collidepoint(x_mouse,y_mouse):
                        if playedTimes>0:
                            Module.printing("JosefinSans-BoldItalic.ttf",40,instruction_image,Variable.nenSangFont,u'Welcome to "Super Memory"',(530,100))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'HOW TO PLAY?',(530,155))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Click "Start" and the game will start after 2s',(530,185))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Fifteen yellow squares will appear randomly.',(530,225))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Your job is to remember the position of them.',(530,265))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'After 15s they will disappear. ',(530,305))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'You need to use your memory to point out ',(530,345))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'all squares\' position.',(530,385))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'You have unlimited time to do it.',(530,425))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Click "End" to see the answer and get gold.',(530,465))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'Each right position gives you 1000 gold.',(530,505))
                            Module.printing("JosefinSans-BoldItalic.ttf",35,instruction_image,Variable.nenSangFont,'You can play again by clicking "Retry".',(530,545))
                            Module.printing("JosefinSans-BoldItalic.ttf",45,instruction_image,Variable.nenSangFont,'Shall we play a game?',(530,590))
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
                                                KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame1_image, (0, 0))
                                                pg.display.flip() 
                                            else:
                                                controlValue=0
                                                watchingTime=False
                                                KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame1_image, (0, 0))
                                                pg.display.flip() 
                    if quit1_rect.collidepoint(x_mouse,y_mouse): # cái này thoát game
                        KingOfBet_LostInPokemonWorld.channel2.fadeout(1000)
                        KingOfBet_LostInPokemonWorld.channel1.set_volume(1)
                        KingOfBet_LostInPokemonWorld.channel1.play(KingOfBet_LostInPokemonWorld.nhapTen,-1)
                        miniGame.minigame(ID,playerName,Money)
            # vẽ hình yêu cầu
            if event.type == pg.MOUSEBUTTONUP : # người dùng click chuột
                if pg.mouse.get_pressed and controlValue==3 :   
                    x_mouse,y_mouse=pg.mouse.get_pos()
                    for i in range(0,colum*row):  # kiểm tra ô nào được chọn
                        # cái chỗ này là bấm trúng ô
                        if  squares[i].collidepoint(x_mouse,y_mouse):  # xác định vị trí của ô đó rồi lấy màu hiện tại ở ô đó
                            x,y=squares_xy[i]
                            x+=25
                            y+=25
                            current_color=BG_minigame1_image.get_at((x,y))[:3]
                            if current_color==black_color and selectCount<numberOfSquares: # nếu màu đen và số lượng ô màu vàng ít hơn số ô có thể có thì đổi màu của ô
                                BG_minigame1_image.blit(yellowSquare_image,squares_xy[i])
                                selectCount+=1 # tăng số ô đã tô màu
                            elif current_color==yellow_color and selectCount<=numberOfSquares:# nếu ô màu vàng và số lượng ô nhỏ hơn hoặc bằng số lượng ô có thể có thì đổi màu ô
                                BG_minigame1_image.blit(blackSquare_image,squares_xy[i])
                                selectCount-=1 # giảm số ô đã tô màu
                    # Kiểm tra hình đã vẽ
                    if finishButton_rect.collidepoint(x_mouse,y_mouse) and controlValue==3: # Nếu nhấn nút kết thúc thì xuất điểm số và tiền của người chơi
                        controlValue+=1
                        # Kiểm tra số ô đúng
                        for i in range(0,99):
                            x_squares,y_squares=squares_xy[i]
                            y_squares+=25
                            x_squares+=25
                            # lấy màu của ô đó
                            current_color=BG_minigame1_image.get_at((x_squares,y_squares))[:3]
                            if squares_xy[i] in random_squares:
                                if current_color==yellow_color:
                                    right_squares+=1
                                else:
                                    BG_minigame1_image.blit(redSquare_image,squares_xy[i])
                            else:
                                if current_color==yellow_color:
                                    BG_minigame1_image.blit(redSquare_image,squares_xy[i])
                        # Tính tiền
                        Money=Money+3*right_squares
                        Variable.playerMoneys[ID-1]=Money
                        Module.writeData(ID)
                        # xuất tiền 
                        if right_squares==numberOfSquares:
                            Module.printing("JosefinSans-BoldItalic.ttf",40,BG_minigame1_image,Variable.YELLOW,'You Win the Game!!!',(1175,250))
                        else:# tương tự ở trên
                            Module.printing("JosefinSans-BoldItalic.ttf",40,BG_minigame1_image,Variable.YELLOW,'Bad Luck!!!',(1175,250))
                if pg.mouse.get_pressed : # Nếu chuột được nhấn
                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                    if playAgainButton_rect.collidepoint(x_mouse,y_mouse): # cái chỗ này là chơi lại
                        gameTime=pg.time.get_ticks()
                        miniGame1(ID,playerName,Money,1,gameTime,1)
        # Draw Everything
        KingOfBet_LostInPokemonWorld.screen.blit(BG_minigame1_image, (0, 0)) # in background ( câu lệnh này chưa hiểu để làm gì cho lắm ) nhưng mà thiếu thì chả có hình ảnh gì trên màn hình
        KingOfBet_LostInPokemonWorld.screen.blit(goldBoard_image,goldBoard_rect)
        Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,str(Money),(1150,550))
        KingOfBet_LostInPokemonWorld.screen.blit(help_image,help_rect)
        pg.display.flip() # cập nhật màn hình



