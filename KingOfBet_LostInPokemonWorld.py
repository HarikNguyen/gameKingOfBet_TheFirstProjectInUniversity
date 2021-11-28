# -*- coding: utf-8 -*-

"""
Công việc: Tạo game cá cược về đường đua có kèm theo một số minigame.
    Đối tượng người dung: game thủ và sinh viên của lớp CTT4 - KHTN.
    Nền tảng: Hệ điều hành Windows.
    Môi trường sử dụng: Giao diện đồ họa người chơi.
    Các chức năng cần có: - Tạo ra một game chính có các bộ nhân vật do người chơi chọn đua trên một bản đồ, người chơi sẽ đặt cược vào nhân vật tùy ý.
                          - Tạo ra tối thiểu 3 minigame để cung cấp tiền ban đầu cho người chơi sử dụng trong game chính.
                          - Lưu trữ số tiền và tên nhân vật của người chơi cho lần chơi lần sau.
    Thử nghiệm & Tìm kiếm lỗi:
    Người phát triên: Nhóm 6 - Lớp NMCNTT- CTT4A- Trường đại học Khoa học Tự nhiên- Đại học Quốc gia thành phố Hồ Chí Minh.
    Liên hệ:  504e8a28.student.hcmus.edu.vn@apac.teams.ms
              https://discord.gg/qAuvXHgZ .
"""


__version__= 1.4
__maintainer__ = "facebook.com/topsiu1.ds"
__status__= "Final"
__date__ = "11/1/2021"



import pygame as pg
import sys , os
import time , random,classes,webbrowser
from pygame.locals import*
from Module import*
from Variable import*
from classes import*
import miniGame1,miniGame2,miniGame3,mainGame,miniGame,database
# Khởi tạo khung hình
pg.init()
screen = pg.display.set_mode((windowWidth,windowHeight),pg.RESIZABLE)
pg.display.set_caption("King of Bet!!!")
pg.mouse.set_visible(1)
# Đồng hồ:
clock = pg.time.Clock()
# Khởi tạo hình ảnh:
goldBoard_image,goldBoard_rect=load_image("goldBoard.png","logIn")
goldBoard_rect.center=(1200,50)
mainGameBG_image,mainGameBG_rect =load_image("mainBackground.png","logIn")
logIn_tron_image,logIn_tron_rect=load_image("logIn_tron.png","logIn")
quayTroLai_image,quayTroLai_rect=load_image("quayTroLai.png","logIn")
minigame_image,minigame_rect=load_image("minigame.png","logIn")
maingame_image,maingame_rect=load_image("maingame.png","logIn")
store_image,store_rect=load_image('store.png',"logIn")
nhapTNV_image,nhapTNV_rect=load_image("nhapTenNhanVat.png","logIn")
tenNVText_image,tenNVText_rect=load_image("tenNVText.png","logIn")
blankName_image,blankName_rect=load_image("blank_name.png","logIn")
blankPassword_image,blankPassword_rect=load_image("blankPassword.png","logIn")
enterPassword_image,enterPassword_rect=load_image("enterPassword.png","logIn")
enterCode_image,enterCode_rect=load_image("codeEnter.png","logIn")
enterCode_rect.center=(660,250)
tenNV_image,tenNV_rect=load_image("tenNV.png","logIn")
blankTenNV_image,blankTenNV_rect=load_image("blankTenNV.png","logIn")
bieuTuong_image,bieuTuong_rect=load_image("bieuTuong.png","logIn")
newPlayer_image,newPlayer_rect=load_image("newPlayer.png","logIn")
oldPlayer_image,oldPlayer_rect=load_image("oldPlayer.png","logIn")
clickToStart_image,clickToStart_rect=load_image("clickToStart.png","logIn")
quit_image,quit_rect=load_image('quit.png','logIn')
quit_rect.center=(1100,600)
start_image,start_rect=load_image("start.png","logIn")
logo_image,logo_rect=load_image("teamLogo.png","logIn")
logo_mini,logo_miniRect=load_image("teamLogoMini.png","logIn")
createAccount_image,createAccount_rect=load_image("createAccount.png","logIn")
clear_image,clear_rect=load_image("clear.png","logIn")
setChoose=True
channel1=pygame.mixer.Channel(1)
channel2=pygame.mixer.Channel(2)
channel3=pygame.mixer.Channel(3)
nhannut=load_sound("nhannut.mp3")
nhapTen=load_sound('nhapten.mp3')
intro=load_sound('intro.wav')
soXo = load_sound('sx.wav')
stunSound=load_sound('stun.mp3')
teleportSound=load_sound('teleport.mp3')
bootSound=load_sound('boot.mp3')
anmungSound=load_sound('anmung.mp3')
minigame1Sound=Module.load_sound('minigame1.mp3')
minigame2Sound=Module.load_sound('minigame2.mp3')
minigame3Sound=Module.load_sound('minigame3.wav')
maingameSound=Module.load_sound('maingame.wav')
flyObject_image,flyObject_rect=load_image('flyObject.png',"logIn")
flyObject_rect.left=-300
flyObject_rect.top=-300
flyObject2_image,flyObject2_rect=load_image('flyObject2.png',"logIn")
flyObject2_rect.left=250
flyObject2_rect.top=-600
def main(ID,playerName,Money):
    """Chạy khi người chơi đã hoàn thành thiết lập tên."""
    channel1.set_volume(1)
    channel1.play(nhapTen,-1)
    # Hình ảnh:
    history_image,history_rect=Module.load_image("history.png","mainGame")
    bettingHistory_image,bettingHistory_rect=Module.load_image("bettingHistory.png","mainGame")
    bettingHistory_rect.center=(670,400)
    quayTroLai_rect.center=(250,650)
    minigame_rect.center=(1150,300)
    maingame_rect.center=(1150,150)
    store_rect.center=(1150,450)
    history_rect.center=(1150,600)
    goldBoard_rect.center=(1200,50)
    nut=['no','no','no','no','no']
    left=500
    top=-800
    pg.display.flip()
    while True:
        screen.blit(mainGameBG_image,(0,0))
        screen.blit(flyObject_image,flyObject_rect)
        screen.blit(flyObject2_image,flyObject2_rect)
        screen.blit(flyObject_image,flyObject2_rect)
        screen.blit(flyObject2_image,flyObject_rect)
        screen.blit(flyObject_image,(left,top))
        screen.blit(flyObject2_image,(left,top))
        screen.blit(goldBoard_image,goldBoard_rect)
        printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),(1170,50))
        flyObject_rect.top+=8
        flyObject_rect.left+=8
        flyObject2_rect.top+=12
        flyObject2_rect.left+=12
        left+=4
        top+=4
        if flyObject_rect.top>=650:
            flyObject_rect.left=-300
            flyObject_rect.top=-300
        if flyObject2_rect.top>=800:
            flyObject2_rect.left=250
            flyObject2_rect.top=-600
        if top>=650:
            left=650
            top=-600
        x_mouse,y_mouse=pg.mouse.get_pos()
        if minigame_rect.collidepoint(x_mouse,y_mouse):
            nut[0]='yes'
        else:
            nut[0]='no'
        if maingame_rect.collidepoint(x_mouse,y_mouse) :
            nut[1]='yes'
        else:
            nut[1]='no'
        if quayTroLai_rect.collidepoint(x_mouse,y_mouse) :
            nut[2]='yes'
        else:
            nut[2]='no'
        if store_rect.collidepoint(x_mouse,y_mouse) :
            nut[3]='yes'
        else:
            nut[3]='no'
        if history_rect.collidepoint(x_mouse,y_mouse) :
            nut[4]='yes'
        else:
            nut[4]='no'
        if nut[0]=='yes':
            screen.blit(pg.transform.scale(minigame_image,(minigame_rect.width+10,minigame_rect.height+10)),minigame_rect)
        else:
            screen.blit(minigame_image,minigame_rect)
        if nut[1]=='yes':
            screen.blit(pg.transform.scale(maingame_image,(maingame_rect.width+10,maingame_rect.height+10)),maingame_rect)
        else:
            screen.blit(maingame_image,maingame_rect)
        if nut[2]=='yes':
            screen.blit(pg.transform.scale(quayTroLai_image,(quayTroLai_rect.width+10,quayTroLai_rect.height+10)),quayTroLai_rect)
        else:
            screen.blit(quayTroLai_image,quayTroLai_rect)
        if nut[3]=='yes':
            screen.blit(pg.transform.scale(store_image,(store_rect.width+10,store_rect.height+10)),store_rect)
        else:
            screen.blit(store_image,store_rect)
        if nut[4]=='yes':
            screen.blit(pg.transform.scale(history_image,(history_rect.width+10,history_rect.height+10)),history_rect)
        else:
            screen.blit(history_image,history_rect)
        pg.display.flip()
        current_time=pg.time.get_ticks()
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if pg.mouse.get_pressed():
                    channel3.play(nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos()
                if minigame_rect.collidepoint(x_mouse,y_mouse):
                    miniGame.minigame(ID,playerName,Money)
                if quayTroLai_rect.collidepoint(x_mouse,y_mouse):
                    channel1.fadeout(1000)
                    channel2.set_volume(1)
                    channel2.play(soXo,-1)
                    logIn()
                if maingame_rect.collidepoint(x_mouse,y_mouse):
                    channel1.fadeout(1000)
                    if not Variable.muteOrNot:
                        channel2.set_volume(1)
                    channel2.play(maingameSound,-1)
                    mainGame.mainGame(ID,playerName,Money)
                if store_rect.collidepoint(x_mouse,y_mouse):
                    store(ID,playerName,Money)
                if history_rect.collidepoint(x_mouse,y_mouse):
                    screen.fill((250,229,89))
                    screen.blit(bettingHistory_image,bettingHistory_rect)
                    screen.blit(quayTroLai_image,quayTroLai_rect)
                    printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,'Pokemon   Bet    Result   Prediction',(bettingHistory_rect.left+250,bettingHistory_rect.top+120))
                    resultData=[]
                    betName=[]
                    betMoney=[]
                    betResult=[]
                    betPrediction=[]
                    resultData.extend((betName,betMoney,betResult,betPrediction))
                    data=cuaHangData(playerName)
                    history(data,resultData)
                    for i in range(0,len(betMoney)):
                        printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,f'{resultData[0][i]}       {resultData[1][i]}      {resultData[2][i]}      {resultData[3][i]}',(bettingHistory_rect.left+250,bettingHistory_rect.top+i*40+150))
                    pg.display.flip()
                    bettingHistoryTime=True
                    while bettingHistoryTime:
                        for event in pg.event.get():
                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                pg.display.quit()
                                pg.quit()
                                sys.exit()
                            if event.type == pg.MOUSEBUTTONUP:
                                if pg.mouse.get_pressed():
                                    channel3.play(nhannut)
                                    x_mouse,y_mouse=pg.mouse.get_pos()
                                    if quayTroLai_rect.collidepoint(x_mouse,y_mouse):
                                        bettingHistory=False
                                        main(ID,playerName,Money)


def store(ID,playerName,Money) :
    data=cuaHangData(playerName)
    storeBack_image,storeBack_rect=Module.load_image("storeBack.png","logIn")
    storeNext_image,storeNext_rect=Module.load_image("storeNext.png","logIn")
    storeBackground_image,storeBackground_rect=load_image("storeBackground.png","logIn")
    blueCrewmate_image,blueCrewmate_rect=load_image('bieuTuongBlueCrewmate.png',"logIn")
    blueCrewmate_rect.center=(240,230)
    redCrewmate_image,redCrewmate_rect=load_image('bieuTuongRedCrewmate.png',"logIn")
    redCrewmate_rect.center=(480,230)
    yellowCrewmate_image,yellowCrewmate_rect=load_image('bieuTuongYellowCrewmate.png',"logIn")
    yellowCrewmate_rect.center=(700,230)
    shark_image,shark_rect=load_image("bieuTuongShark.png","logIn")
    shark_rect.center=(910,230)
    narancia_image,narancia_rect=load_image("bieuTuongNarancia.png","logIn")
    narancia_rect.center=(1150,230)
    penguin_image,penguin_rect=load_image("bieuTuongPenguin.png","logIn")
    penguin_rect.center=(240,520)
    polarBear_image,polarBear_rect=load_image("bieuTuongPolarBear.png","logIn")
    polarBear_rect.center=(450,520)
    girl_image,girl_rect=load_image("bieuTuongGirl.png","logIn")
    girl_rect.center=(680,520)
    cheem_image,cheem_rect=load_image("bieuTuongCheem.png","logIn")
    cheem_rect.center=(920,520)
    buff1_image,buff1_rect=load_image("oneRandomBuff.png","logIn")
    buff1_rect.center=(1150,530)
    buff2_image,buff2_rect=load_image("packOf50_Buff.png","logIn")
    buff2_rect.center=(240,240)
    buff3_image,buff3_rect=load_image("packOf60_Buff.png","logIn")
    buff3_rect.center=(480,240)
    gold_image,gold_rect=load_image('codeIcon.png','logIn')
    gold_rect.center=(950,65)
    instruction_image,instruction_rect=Module.load_image("instruction.png","logIn")
    instruction_rect.center=(650,400)
    xButton_image,xButton_rect=Module.load_image("xButton.png","logIn")
    xButton_rect.center=(1050,150)
    bieutuong=[blueCrewmate_image,redCrewmate_image,yellowCrewmate_image,shark_image,narancia_image,penguin_image,polarBear_image,girl_image,cheem_image,buff1_image,buff2_image,buff3_image]
    bieutuong_rect=[blueCrewmate_rect,redCrewmate_rect,yellowCrewmate_rect,shark_rect,narancia_rect,penguin_rect,polarBear_rect,girl_rect,cheem_rect,buff1_rect,buff2_rect,buff3_rect]
    sold_image,sold_rect=Module.load_image('sold.png',"logIn")
    soldPos=[(138.5,148.5),(370.5,148.5),(602.5,148.5),(834.5,148.5),(1046.5,148.5),(138.5,430),(370.5,430),(602.5,430),(834.5,430),(1046.5,430)]
    giaTien=[10,10,10,10,10,10,10,1000,10,100,300,600]
    next_image,next_rect=load_image("next.png","logIn")
    exchange_image,exchange_rect=load_image('OKButton.png',"logIn")
    exchange_rect.center=(650,400)
    buyCode_rect=pg.Rect(871,592,95,56)
    storeNext_rect.center=(1250,65)
    goldBoard_rect.center=(330,70)
    storeBack_rect.center=(1050,65)
    tienRect=(300,70)
    trang1=True
    trang2=False
    buying=False
    nut=['no','no']
    chon=['khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong','khong']
    while True:
        clock.tick(60)
        if trang1:
            screen.blit(storeBackground_image,storeBackground_rect)
            screen.blit(storeBack_image,storeBack_rect)
            screen.blit(storeNext_image,storeNext_rect)
            screen.blit(gold_image,gold_rect)
            for i in range(0,10):
                screen.blit(bieutuong[i],bieutuong_rect[i])
                if data[i+2]=='sold':
                    screen.blit(sold_image,soldPos[i])
                printing('JosefinSans-BoldItalic.ttf',36,screen,nenToiFont,str(giaTien[i]),(240+230*(i-int(i/5)*5),380+int(i/5)*290))
            screen.blit(goldBoard_image,goldBoard_rect)
            printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),tienRect)
            pg.display.flip()
            buying=True
            while buying:
                for event in pg.event.get():
                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if event.type==pg.MOUSEBUTTONUP:
                        if pg.mouse.get_pressed():
                            channel3.play(nhannut)
                            x_mouse,y_mouse=pg.mouse.get_pos()
                            for rect in range(0,10):
                                if bieutuong_rect[rect].collidepoint(x_mouse,y_mouse):
                                    if chon[rect]=='khong':
                                        for i in chon:
                                            i='khong'
                                        chon[rect]='co'
                                    elif chon[rect]=='co':
                                        chon[rect]='khong'
                                        if giaTien[rect]<=Money and data[rect+2]=='notsold':
                                           data[rect+2]='sold'
                                           Money=Money-giaTien[rect]
                                           Variable.playerMoneys[ID-1]=Money
                                           writeData(ID)
                                           updateCuaHang(playerName,data)
                                           screen.blit(storeBackground_image,storeBackground_rect)
                                           screen.blit(storeBack_image,storeBack_rect)
                                           screen.blit(storeNext_image,storeNext_rect)
                                           screen.blit(gold_image,gold_rect)
                                           screen.blit(goldBoard_image,goldBoard_rect)
                                           printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),tienRect)
                                           for i in range(0,10):
                                               screen.blit(bieutuong[i],bieutuong_rect[i])
                                               if data[i+2]=='sold':
                                                   screen.blit(sold_image,soldPos[i]) 
                                               printing('JosefinSans-BoldItalic.ttf',36,screen,nenToiFont,str(giaTien[i]),(240+230*(i-int(i/5)*5),380+int(i/5)*290))
                                               pg.display.flip()
                                        elif giaTien[rect]>Money and data[rect+2]=='notsold':
                                            printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,'You dont\'t have enough money!!!',(750,95))
                                            pg.display.flip()
                                elif storeBack_rect.collidepoint(x_mouse,y_mouse):
                                    updateCuaHang(playerName,data)
                                    main(ID,playerName,Money)
                                elif storeNext_rect.collidepoint(x_mouse,y_mouse):
                                    trang1=False
                                    trang2=True
                                    buying=False
                                elif gold_rect.collidepoint(x_mouse,y_mouse):
                                    screen.blit(instruction_image, instruction_rect)
                                    screen.blit(xButton_image,xButton_rect)
                                    screen.blit(exchange_image,exchange_rect)
                                    screen.blit(enterCode_image,enterCode_rect)
                                    nhap=False
                                    giftCode=''
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
                                                    channel3.play(nhannut)
                                                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                                                    if xButton_rect.collidepoint(x_mouse,y_mouse): #cái này bắt đầu chơi   
                                                            watchingTime=False
                                                            screen.blit(storeBackground_image,storeBackground_rect)
                                                            screen.blit(storeBack_image,storeBack_rect)
                                                            screen.blit(storeNext_image,storeNext_rect)
                                                            screen.blit(gold_image,gold_rect)
                                                            for i in range(0,10):
                                                                screen.blit(bieutuong[i],bieutuong_rect[i])
                                                                if data[i+2]=='sold':
                                                                    screen.blit(sold_image,soldPos[i])
                                                                printing('JosefinSans-BoldItalic.ttf',36,screen,nenToiFont,str(giaTien[i]),(240+230*(i-int(i/5)*5),380+int(i/5)*290))
                                                            screen.blit(goldBoard_image,goldBoard_rect)
                                                            printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),tienRect)
                                                            pg.display.flip()
                                                    if enterCode_rect.collidepoint(x_mouse,y_mouse):
                                                        nhap=True
                                                    if exchange_rect.collidepoint(x_mouse,y_mouse):
                                                        screen.blit(instruction_image, instruction_rect)
                                                        screen.blit(xButton_image,xButton_rect)
                                                        screen.blit(enterCode_image,enterCode_rect)
                                                        screen.blit(exchange_image,exchange_rect)
                                                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                        if giftCode =='YRC100G' and data[22]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+100
                                                           data[22]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           pg.display.flip()
                                                           writeData(ID)
                                                        elif giftCode =='YRC1000G' and data[23]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[23]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='YRC10000G' and data[24]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+10000
                                                           data[24]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='QUAMONTHNMCNTT1' and data[25]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[25]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='DAIHOCNHANLAM' and data[26]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1
                                                           data[26]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        else:
                                                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your code is wrong or already use.",(700,550))
                                                            pg.display.flip()
                                                        updateCuaHang(playerName,data) 
                                                    if buyCode_rect.collidepoint(x_mouse,y_mouse):
                                                        webbrowser.open('http://lostinthepokemonworld.ga/', new=1, autoraise=True)
                                            if event.type == pg.KEYDOWN:
                                                channel3.play(nhannut)
                                                if event.key == pg.K_BACKSPACE:
                                                    giftCode = giftCode[:-1]
                                                    screen.blit(instruction_image, instruction_rect)
                                                    screen.blit(xButton_image,xButton_rect)
                                                    screen.blit(enterCode_image,enterCode_rect)
                                                    screen.blit(exchange_image,exchange_rect)
                                                    printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                    pg.display.flip()
                                                elif event.key==pg.K_RETURN:
                                                        screen.blit(instruction_image, instruction_rect)
                                                        screen.blit(xButton_image,xButton_rect)
                                                        screen.blit(enterCode_image,enterCode_rect)
                                                        screen.blit(exchange_image,exchange_rect)
                                                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                        if giftCode =='YRC100G' and data[22]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+100
                                                           data[22]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           pg.display.flip()
                                                           writeData(ID)
                                                        elif giftCode =='YRC1000G' and data[23]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[23]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='YRC10000G' and data[24]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+10000
                                                           data[24]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='QUAMONTHNMCNTT1' and data[25]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[25]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='DAIHOCNHANLAM' and data[26]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1
                                                           data[26]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        else:
                                                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your code is wrong or already used.",(700,550))
                                                            pg.display.flip()
                                                        updateCuaHang(playerName,data)
                                                else:
                                                    if event.unicode!=' ':
                                                        giftCode += event.unicode
                                                    screen.blit(instruction_image, instruction_rect)
                                                    screen.blit(xButton_image,xButton_rect)
                                                    screen.blit(enterCode_image,enterCode_rect)
                                                    screen.blit(exchange_image,exchange_rect)
                                                    printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                    pg.display.flip()
                                               
        if trang2:
            screen.blit(storeBackground_image,storeBackground_rect)
            screen.blit(storeBack_image,storeBack_rect)
            screen.blit(gold_image,gold_rect)
            for i in range(10,len(bieutuong)):
                screen.blit(bieutuong[i],bieutuong_rect[i])
                if data[i+2]=='sold':
                    screen.blit(sold_image,soldPos[i-10])
                printing('JosefinSans-BoldItalic.ttf',36,screen,nenToiFont,str(giaTien[i]),(240+230*(i-10-int((i-10)/5)*5),380+int((i-10)/5)*290))
            screen.blit(goldBoard_image,goldBoard_rect)
            printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),tienRect)
            pg.display.flip()
            buying=True
            while buying:
                for event in pg.event.get():
                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if event.type==pg.MOUSEBUTTONUP:
                        if pg.mouse.get_pressed():
                            channel3.play(nhannut)
                            x_mouse,y_mouse=pg.mouse.get_pos()
                            for rect in range(10,len(bieutuong)):
                                if bieutuong_rect[rect].collidepoint(x_mouse,y_mouse):
                                    if chon[rect]=='khong':
                                        chon[rect]='co'
                                    elif chon[rect]=='co':
                                        if giaTien[rect]<=Money and data[rect+2]=='notsold':
                                           data[rect+2]='sold'
                                           Money=Money-giaTien[rect]
                                           Variable.playerMoneys[ID-1]=Money
                                           writeData(ID)
                                           updateCuaHang(playerName,data)
                                           screen.blit(storeBackground_image,storeBackground_rect)
                                           screen.blit(storeBack_image,storeBack_rect)
                                           screen.blit(storeNext_image,storeNext_rect)
                                           screen.blit(gold_image,gold_rect)
                                           screen.blit(goldBoard_image,goldBoard_rect)
                                           printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),tienRect)
                                           for i in range(10,len(bieutuong)):
                                                screen.blit(bieutuong[i],bieutuong_rect[i])
                                                if data[i+2]=='sold':
                                                    screen.blit(sold_image,soldPos[i-10])
                                                printing('JosefinSans-BoldItalic.ttf',36,screen,nenToiFont,str(giaTien[i]),(240+230*(i-10-int((i-10)/5)*5),380+int((i-10)/5)*290))
                                           pg.display.flip()
                                        elif giaTien[rect]>Money and data[rect+2]=='notsold':
                                            printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,'You dont\'t have enough money!!!',(750,95))
                                            pg.display.flip()
                                elif storeBack_rect.collidepoint(x_mouse,y_mouse):
                                    trang1=True
                                    trang2=False
                                    buying=False   
                                elif gold_rect.collidepoint(x_mouse,y_mouse):
                                    screen.blit(instruction_image, instruction_rect)
                                    screen.blit(xButton_image,xButton_rect)
                                    screen.blit(exchange_image,exchange_rect)
                                    screen.blit(enterCode_image,enterCode_rect)
                                    pg.display.flip()
                                    giftCode=''
                                    watchingTime=True
                                    while watchingTime:
                                        for event in pg.event.get():
                                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                                pg.display.quit()
                                                pg.quit()
                                                sys.exit()
                                            if event.type == pg.MOUSEBUTTONUP: # Nếu chuột được nhấn và đã xóa hình ảnh
                                                if pg.mouse.get_pressed:
                                                    channel3.play(nhannut)
                                                    channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    x_mouse,y_mouse=pg.mouse.get_pos() # lấy vị trí chuột
                                                    if xButton_rect.collidepoint(x_mouse,y_mouse): #cái này bắt đầu chơi   
                                                            watchingTime=False
                                                            screen.blit(storeBackground_image,storeBackground_rect)
                                                            screen.blit(storeBack_image,storeBack_rect)
                                                            screen.blit(gold_image,gold_rect)
                                                            for i in range(10,len(bieutuong)):
                                                                screen.blit(bieutuong[i],bieutuong_rect[i])
                                                                if data[i+2]=='sold':
                                                                    screen.blit(sold_image,soldPos[i-10])
                                                                printing('JosefinSans-BoldItalic.ttf',36,screen,nenToiFont,str(giaTien[i]),(240+230*(i-10-int((i-10)/5)*5),380+int((i-10)/5)*290))
                                                            screen.blit(goldBoard_image,goldBoard_rect)
                                                            printing('JosefinSans-BoldItalic.ttf',20,screen,nenSangFont,str(Money),tienRect)
                                                            pg.display.flip()
                                                    if enterCode_rect.collidepoint(x_mouse,y_mouse):
                                                        nhap=True
                                                    if exchange_rect.collidepoint(x_mouse,y_mouse):
                                                        screen.blit(instruction_image, instruction_rect)
                                                        screen.blit(xButton_image,xButton_rect)
                                                        screen.blit(enterCode_image,enterCode_rect)
                                                        screen.blit(exchange_image,exchange_rect)
                                                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                        if giftCode =='YRC100G' and data[22]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+100
                                                           data[22]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           pg.display.flip()
                                                           writeData(ID)
                                                        elif giftCode =='YRC1000G' and data[23]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[23]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='YRC10000G' and data[24]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+10000
                                                           data[24]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='QUAMONTHNMCNTT1' and data[25]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[25]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='DAIHOCNHANLAM' and data[26]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1
                                                           data[26]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        else:
                                                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your code is wrong or already used.",(700,550))
                                                            pg.display.flip()
                                                        updateCuaHang(playerName,data)
                                                    if buyCode_rect.collidepoint(x_mouse,y_mouse):
                                                        webbrowser.open('http://lostinthepokemonworld.ga/', new=1, autoraise=True)
                                            if event.type == pg.KEYDOWN:
                                                channel3.play(nhannut)
                                                if event.key == pg.K_BACKSPACE:
                                                    giftCode = giftCode[:-1]
                                                    screen.blit(instruction_image, instruction_rect)
                                                    screen.blit(xButton_image,xButton_rect)
                                                    screen.blit(enterCode_image,enterCode_rect)
                                                    screen.blit(exchange_image,exchange_rect)
                                                    printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                    pg.display.flip()
                                                elif event.key==pg.K_RETURN:
                                                        screen.blit(instruction_image, instruction_rect)
                                                        screen.blit(xButton_image,xButton_rect)
                                                        screen.blit(enterCode_image,enterCode_rect)
                                                        screen.blit(exchange_image,exchange_rect)
                                                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                        if giftCode =='YRC100G' and data[22]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+100
                                                           data[22]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           pg.display.flip()
                                                           writeData(ID)
                                                        elif giftCode =='YRC1000G' and data[23]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[23]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='YRC10000G' and data[24]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+10000
                                                           data[24]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip
                                                        elif giftCode =='QUAMONTHNMCNTT1' and data[25]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1000
                                                           data[25]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        elif giftCode =='DAIHOCNHANLAM' and data[26]=='no':
                                                           printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Thanks for purchasing out product.",(700,550))
                                                           Money=Money+1
                                                           data[26]='yes'
                                                           Variable.playerMoneys[ID-1]=Money
                                                           writeData(ID)
                                                           pg.display.flip()
                                                        else:
                                                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your code is wrong or already used.",(700,550))
                                                            pg.display.flip()
                                                        updateCuaHang(playerName,data)
                                                else:
                                                    if event.unicode!=' ':
                                                        giftCode += event.unicode
                                                    screen.blit(instruction_image, instruction_rect)
                                                    screen.blit(xButton_image,xButton_rect)
                                                    screen.blit(enterCode_image,enterCode_rect)
                                                    screen.blit(exchange_image,exchange_rect)
                                                    printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,giftCode,enterCode_rect.center)
                                                    pg.display.flip()
def newPlayer():
    """ Hàm này được gọi khi muốn thêm người chơi mới."""
    # biến:
    storeBack_image,storeBack_rect=Module.load_image("storeBack.png","logIn")
    storeNext_image,storeNext_rect=Module.load_image("storeNext.png","logIn")
    FPSCLOCK=pg.time.Clock()
    getName=False
    getPassword1=False
    getPassword2=False
    noName=None
    password1=''
    password2=''
    show='No'
    blindPassword1=''
    blindPassword2=''
    setBG=True
    playerName=""
    screen.blit(createAccount_image,(0,0))
    # Khởi tạo hình ảnh:
    storeBack_rect.center=(1100,600)
    storeNext_rect.center=(1100,500)
    clear_rect.center=(1100,550)
    userName_rect=pg.Rect(450,210,500,75)
    pass1_rect=pg.Rect(450,392,500,75)
    pass2_rect=pg.Rect(450,576,500,75)
    nut=['no','no']
    pg.display.update()
    while True: 
        screen.blit(clear_image,clear_rect)
        x_mouse,y_mouse=pg.mouse.get_pos()
        if storeBack_rect.collidepoint(x_mouse,y_mouse):
            nut[1]='yes'
        else:
            nut[1]='no'
        if storeNext_rect.collidepoint(x_mouse,y_mouse) :
            nut[0]='yes'
        else:
            nut[0]='no'
        if nut[0]=='yes':
            screen.blit(pg.transform.scale(storeNext_image,(storeNext_rect.width+10,storeNext_rect.height+10)),storeNext_rect)
        else:
            screen.blit(storeNext_image,storeNext_rect)
        if nut[1]=='yes':
            screen.blit(pg.transform.scale(storeBack_image,(storeBack_rect.width+10,storeBack_rect.height+10)),storeBack_rect)
        else:
            screen.blit(storeBack_image,storeBack_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if pg.mouse.get_pressed():
                    channel3.play(nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos()
                if userName_rect.collidepoint(x_mouse,y_mouse):
                    getPassword1=False
                    getPassword2=False
                    getName=True
                if pass1_rect.collidepoint(x_mouse,y_mouse):
                    getName=False
                    getPassword2=False
                    getPassword1=True
                if pass2_rect.collidepoint(x_mouse,y_mouse):
                    getName=False
                    getPassword1=False
                    getPassword2=True
                if storeBack_rect.collidepoint(x_mouse,y_mouse):
                    logIn()# cái chỗ này quay lại chỗ chọn new player với oldplayer
                if storeNext_rect.collidepoint(x_mouse,y_mouse) :
                    if password1=='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Password!!!",(700,490))
                    elif password2=='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please ReEnter Your Password!!!",(700,690))
                    if playerName=="":
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Username!!!",(700,310))
                    if len(playerName)<6 and len(playerName)!='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your Username must has at least 6 letters!!!",(700,310))
                    elif password1!="" :
                        if password1==password2:
                            data=[playerName,password1,'sold','sold','sold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','0']
                            data.extend(['no','no','no','no','no'])
                            updateCuaHang(playerName,data)
                            Money=0
                            getName=False
                            database.inputTable_user(playerName, Money, 0,0,False,False,False,False,False)
                            readData()
                            channel2.fadeout(1000)
                            channel1.set_volume(1)
                            channel1.play(nhapTen,-1)
                            ID = len(playerID)
                            start_rect=-1000
                            main(ID,playerName,Money)
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your passwords don't matched!!!",(700,690))
            if event.type == pg.KEYDOWN:
                channel3.play(nhannut)
                if event.key==pg.K_RETURN:
                    if password1=='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Password!!!",(700,490))
                    elif password2=='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please ReEnter Your Password!!!",(700,690))
                    if playerName=="":
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Username!!!",(700,310))
                    if len(playerName)<6:
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your Username must has at least 6 letters!!!",(700,310))
                    elif password1!="":
                        if password1==password2:
                            data=[playerName,password1,'sold','sold','sold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','notsold','0']
                            data.extend(['no','no','no','no','no'])
                            updateCuaHang(playerName,data)
                            Money=0
                            getName=False
                            database.inputTable_user(playerName, Money, 0,0,False,False,False,False,False)
                            readData()
                            channel2.fadeout(1000)
                            channel1.set_volume(1)
                            channel1.play(nhapTen,-1)
                            ID = len(playerID)
                            start_rect=-1000
                            main(ID,playerName,Money)
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your passwords don't matched!!!",(650,600))
                if event.key==pg.K_TAB:
                    if not getName and not getPassword1 and not getPassword2:
                        getName=True
                    elif getPassword1:
                        getPassword2=True
                        getPassword1=False
                    elif getPassword2 :
                        getPassword2=False
                        getName=True
                    elif getName:
                        getPassword1=True
                        getName=False
                if event.key==pg.K_LCTRL:
                    if show=="Yes":
                        show="No"
                    else:
                        show="Yes"
                if getName:
                    if event.key == pg.K_RETURN:# chỗ này vào bảng chọn minigame với maingame
                        getName=False
                    elif event.key == pg.K_BACKSPACE:
                        playerName = playerName[:-1]
                        screen.blit(createAccount_image,(0,0))
                        screen.blit(storeBack_image,storeBack_rect)
                        screen.blit(storeNext_image,storeNext_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(700,250))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password2,(700,615))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword2,(700,615))
                    else:
                        if event.unicode!=' ':
                            if len(playerName)<=12:
                                playerName += event.unicode
                        screen.blit(createAccount_image,(0,0))    
                        screen.blit(storeBack_image,storeBack_rect)
                        screen.blit(storeNext_image,storeNext_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(700,250))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password2,(700,615))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword2,(700,615))
                if getPassword1:
                    if event.key == pg.K_RETURN:# chỗ này vào bảng chọn minigame với maingame                          
                        getPassword1=False
                    elif event.key == pg.K_BACKSPACE:
                        blindPassword1 = blindPassword1[:-1]
                        password1=password1[:-1]
                        screen.blit(createAccount_image,(0,0))   
                        screen.blit(storeBack_image,storeBack_rect)
                        screen.blit(storeNext_image,storeNext_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(700,250))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password2,(700,615))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword2,(700,615))
                    else:
                        password1 += event.unicode
                        if event.unicode!='' and event.unicode!=' ':
                            blindPassword1+='*'
                        screen.blit(createAccount_image,(0,0))   
                        screen.blit(storeBack_image,storeBack_rect)
                        screen.blit(storeNext_image,storeNext_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(700,250))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password2,(700,615))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword2,(700,615))
                if getPassword2:
                    if event.key == pg.K_RETURN:# chỗ này vào bảng chọn minigame với maingame                          
                        getPassword2=False
                    elif event.key == pg.K_BACKSPACE:
                        blindPassword2 = blindPassword2[:-1]
                        password2=password2[:-1]
                        screen.blit(createAccount_image,(0,0))   
                        screen.blit(storeBack_image,storeBack_rect)
                        screen.blit(storeNext_image,storeNext_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(700,250))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password2,(700,615))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword2,(700,615))
                    else:
                        password2 += event.unicode
                        if event.unicode!='' and event.unicode!=' ':
                            blindPassword2+='*'
                        screen.blit(createAccount_image,(0,0))   
                        screen.blit(storeBack_image,storeBack_rect)
                        screen.blit(storeNext_image,storeNext_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(700,250))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password2,(700,615))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword1,(700,430))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword2,(700,615))
        pg.display.flip()

def oldPlayer():
    """Hàm này được gọi khi người chơi muốn chơi tiếp từ lần chơi trước."""
    readData()
    # biến:
    ID=None
    playerName=""
    password=''
    show="No"
    blindPassword=''
    getName=False
    getPassword=False
    playerNameRects=[]
    FPSCLOCK=pg.time.Clock()
    storeBack_image,storeBack_rect=Module.load_image("storeBack.png","logIn")
    storeNext_image,storeNext_rect=Module.load_image("storeNext.png","logIn")
    storeBack_rect.center=(1100,600)
    storeNext_rect.center=(1100,500)
    clear_rect.center=(1100,550)
    nhapTNV_rect.center=(650,100)
    blankName_rect.center=(650,200)
    blankPassword_rect.center=(650,400)
    enterPassword_rect.center=(650,300)
    screen.blit(logIn_tron_image,(0,0))
    screen.blit(blankName_image,blankName_rect)
    screen.blit(blankPassword_image,blankPassword_rect)
    screen.blit(enterPassword_image,enterPassword_rect)
    screen.blit(nhapTNV_image,nhapTNV_rect)       
    nut=['no','no']
    pg.display.update()
    while True:
        screen.blit(clear_image,clear_rect)
        x_mouse,y_mouse=pg.mouse.get_pos()
        if storeBack_rect.collidepoint(x_mouse,y_mouse):
            nut[1]='yes'
        else:
            nut[1]='no'
        if storeNext_rect.collidepoint(x_mouse,y_mouse) :
            nut[0]='yes'
        else:
            nut[0]='no'
        if nut[0]=='yes':
            screen.blit(pg.transform.scale(storeNext_image,(storeNext_rect.width+10,storeNext_rect.height+10)),storeNext_rect)
        else:
            screen.blit(storeNext_image,storeNext_rect)
        if nut[1]=='yes':
            screen.blit(pg.transform.scale(storeBack_image,(storeBack_rect.width+10,storeBack_rect.height+10)),storeBack_rect)
        else:
            screen.blit(storeBack_image,storeBack_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type==pg.MOUSEBUTTONUP:
                if pg.mouse.get_pressed():
                    channel3.play(nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos()
                if blankName_rect.collidepoint(x_mouse,y_mouse):
                    if getPassword:
                        getPassword=False
                    getName=True
                if blankPassword_rect.collidepoint(x_mouse,y_mouse):
                    if getName:
                        getName=False
                    getPassword=True
                if storeBack_rect.collidepoint(x_mouse,y_mouse):
                    logIn()
                if storeNext_rect.collidepoint(x_mouse,y_mouse):
                    if password=='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Password!!!",(650,550))
                    if playerName=="":
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Username!!!",(650,500))
                    if password!="" and playerName!="":
                       try:
                            data=cuaHangData(playerName)
                       except:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your Username doesn\'t exist!!!",(650,600))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please try again or create one!!!",(650,650))
                       else:
                            if data[1]==password:
                                for i in range(0,len(Variable.playerID)):
                                    if Variable.playerNames[i]==playerName:
                                        ID=i+1
                                        Money=Variable.playerMoneys[i]
                                channel2.fadeout(1000)
                                channel1.set_volume(1)
                                channel1.play(nhapTen,-1)
                                start_rect.top=-1000
                                main(ID,playerName,Money)
                            else:
                                printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your Password is wrong!!!",(650,500))
            if event.type == pg.KEYDOWN:
                channel3.play(nhannut)
                if event.key==pg.K_RETURN:
                    if password=='':
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Password!!!",(650,550))
                    if playerName=="":
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please Enter Your Username!!!",(650,500))
                    if password!="" and playerName!="":
                       try:
                            data=cuaHangData(playerName)
                       except:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your Username doesn\'t exist!!!",(650,600))
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Please try again or create one!!!",(650,650))
                       else:
                            if data[1]==password:
                                for i in range(0,len(Variable.playerID)):
                                    if Variable.playerNames[i]==playerName:
                                        ID=i+1
                                        Money=Variable.playerMoneys[i]
                                channel2.fadeout(1000)
                                channel1.set_volume(1)
                                channel1.play(nhapTen,-1)
                                start_rect.top=-1000
                                main(ID,playerName,Money)
                            else:
                                printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,"Your Password is wrong!!!",(650,500))
                if event.key==pg.K_TAB:
                    if not getName and not getPassword:
                        getName=True
                    elif not getName and getPassword:
                        getName=True
                        getPassword=False
                    elif getName and not getPassword:
                        getPassword=True
                        getName=False
                if event.key==pg.K_LCTRL:
                    if show=="Yes":
                        show="No"
                    else:
                        show="Yes"
                if getName:
                    if event.key == pg.K_RETURN:
                        getName=False
                    elif event.key == pg.K_BACKSPACE:
                        playerName = playerName[:-1]
                        screen.blit(logIn_tron_image,(0,0))
                        screen.blit(blankName_image,blankName_rect)
                        screen.blit(blankPassword_image,blankPassword_rect)
                        screen.blit(enterPassword_image,enterPassword_rect)
                        screen.blit(nhapTNV_image,nhapTNV_rect)       
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(650,200))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password,(650,400))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword,(650,400))
                    else:
                        if event.unicode!=' ':
                            playerName += event.unicode
                        screen.blit(logIn_tron_image,(0,0))
                        screen.blit(blankName_image,blankName_rect)
                        screen.blit(blankPassword_image,blankPassword_rect)
                        screen.blit(enterPassword_image,enterPassword_rect)
                        screen.blit(nhapTNV_image,nhapTNV_rect)         
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(650,200))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password,(650,400))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword,(650,400))
                if getPassword:
                    if event.key == pg.K_RETURN:
                        getPassword=False
                    elif event.key == pg.K_BACKSPACE:
                        blindPassword = blindPassword[:-1]
                        password=password[:-1]
                        screen.blit(logIn_tron_image,(0,0))
                        screen.blit(blankName_image,blankName_rect)
                        screen.blit(blankPassword_image,blankPassword_rect)
                        screen.blit(enterPassword_image,enterPassword_rect)
                        screen.blit(nhapTNV_image,nhapTNV_rect)    
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(650,200))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password,(650,400))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword,(650,400))
                    else:
                        password += event.unicode
                        if event.unicode!='' and event.unicode!=' ':
                            blindPassword+='*'
                        screen.blit(logIn_tron_image,(0,0))
                        screen.blit(blankName_image,blankName_rect)
                        screen.blit(blankPassword_image,blankPassword_rect)
                        screen.blit(enterPassword_image,enterPassword_rect)
                        screen.blit(nhapTNV_image,nhapTNV_rect)
                        printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,playerName,(650,200))
                        if show=="Yes":
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,password,(650,400))
                        else:
                            printing('JosefinSans-BoldItalic.ttf',36,screen,nenSangFont,blindPassword,(650,400))
        pg.display.flip()

def logIn():
    """ Hàm này được gọi khi người chơi chạy file .exe .
        This function is called when the .exe file run by the player."""
    # biến:
    global setChoose
    bieuTuong_rect.left=450
    newPlayer_rect.left=450
    newPlayer_rect.top=420
    oldPlayer_rect.left=750
    oldPlayer_rect.top=420
    left=500
    top=-800
    nut=['no','no','no']
    # In background:
    screen.blit(logIn_tron_image,(0,0))
    pg.display.flip()
    # Vòng lặp logIn
    while True:
        clock.tick(60)
        screen.blit(bieuTuong_image,bieuTuong_rect)
        clickToStart_rect.top=420
        clickToStart_rect.left=560
        x_mouse,y_mouse=pg.mouse.get_pos()
        if oldPlayer_rect.collidepoint(x_mouse,y_mouse) :
            nut[1]='yes'
        else:
            nut[1]='no'
        if newPlayer_rect.collidepoint(x_mouse,y_mouse) :
            nut[0]='yes'
        else:
            nut[0]='no'
        if quit_rect.collidepoint(x_mouse,y_mouse) :
            nut[2]='yes'
        else:
            nut[2]='no'
        if not setChoose:
            screen.blit(logIn_tron_image,(0,0))
            screen.blit(flyObject_image,flyObject_rect)
            screen.blit(flyObject2_image,flyObject2_rect)
            screen.blit(flyObject_image,flyObject2_rect)
            screen.blit(flyObject2_image,flyObject_rect)
            screen.blit(flyObject_image,(left,top))
            screen.blit(flyObject2_image,(left,top))
            flyObject_rect.top+=8
            flyObject_rect.left+=8
            flyObject2_rect.top+=12
            flyObject2_rect.left+=12
            left+=4
            top+=4
            if flyObject_rect.top>=650:
                flyObject_rect.left=-300
                flyObject_rect.top=-300
            if flyObject2_rect.top>=800:
                flyObject2_rect.left=250
                flyObject2_rect.top=-600
            if top>=650:
                left=650
                top=-600
            screen.blit(bieuTuong_image,bieuTuong_rect)
            if nut[0]=='no':
                screen.blit(newPlayer_image,newPlayer_rect)
            else:
                screen.blit(pg.transform.scale(newPlayer_image,(newPlayer_rect.width+10,newPlayer_rect.height+10)),newPlayer_rect)
            if nut[1]=='no':
                screen.blit(oldPlayer_image,oldPlayer_rect)
            else:
                screen.blit(pg.transform.scale(oldPlayer_image,(oldPlayer_rect.width+10,oldPlayer_rect.height+10)),oldPlayer_rect)
            if nut[2]=='no':
                screen.blit(quit_image,quit_rect)
            else:
                screen.blit(pg.transform.scale(quit_image,(quit_rect.width+10,quit_rect.height+10)),quit_rect)
            pg.display.update()
        if setChoose:
            screen.blit(clickToStart_image, (560,420))
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if pg.mouse.get_pressed():
                    channel3.play(nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos()
                    if oldPlayer_rect.collidepoint(x_mouse,y_mouse) and setChoose==False:
                        oldPlayer()
                    if newPlayer_rect.collidepoint(x_mouse,y_mouse) and setChoose==False:
                        newPlayer()
                    if quit_rect.collidepoint(x_mouse,y_mouse) and setChoose==False:
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if clickToStart_rect.collidepoint(x_mouse,y_mouse):
                        setChoose=False
        pg.display.flip() 

if __name__=="__main__":
    setLogo=True
    channel1.set_volume(1)
    channel1.play(intro,1)
    if setLogo:
        fade_in(screen,logo_image,(400,180))
        setLogo=False
    setLogIn=True
    i=0
    bieuTuong_rect.left=450
    channel1.fadeout(1500)
    channel2.set_volume(1)
    channel2.play(soXo,-1)
    while setLogIn:
        screen.blit(logIn_tron_image,(0,0))
        if bieuTuong_rect.bottom<450:
            screen.blit(bieuTuong_image,bieuTuong_rect)
            bieuTuong_rect.bottom+=2
        else:
            screen.blit(bieuTuong_image,bieuTuong_rect)
        if i<256:
            clickToStart_image.set_alpha(i)
            screen.blit(clickToStart_image, (560,420))
            i+=4
        else:
            setLogIn=False
        clock.tick(30)
        pg.display.flip()
    logIn()
   