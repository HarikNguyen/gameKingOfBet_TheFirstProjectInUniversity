# -*- coding: utf-8 -*-

import pygame as pg
from pygame.locals import*
import Variable
import os,sys,database

# Hàm tải lên hình ảnh.
def load_image(name,thumuc="",colorkey=None):
    """Hàm này để tải file hình ảnh vào file chương trình"""
    if thumuc!="":
        fullname = os.path.join(Variable.imageDir,thumuc, name) # tạo đường dẫn đến file
    else:
        fullname = os.path.join(Variable.imageDir, name)# tạo đường dẫn đến file
    try:
        image = pg.image.load(fullname).convert_alpha() # tải file vào game và cài đặt một số đặc điểm ảnh
    except pg.error as message: # cái này để bị lỗi sẽ báo cho mình
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey is not None: # cái này chưa hiểu lắm nhưng kiểu dùng cho transparent ảnh
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect() # xuất ảnh với khối hình của ảnh

# Hàm tải lên âm thanh.
def load_sound(name,thumuc=""):
    """Hàm này để tải âm thanh vào file chương trình"""
    class NoneSound: # tạo cái file âm thanh mặc định
        def play(self): pass
    if not pg.mixer: # nếu không có thư viện mixer thì chạy file mặc định
        return NoneSound()
    if thumuc!= "":
        fullname = os.path.join(Variable.soundDir,thumuc, name) # tạo đường dẫn đến file
    else:
        fullname = os.path.join(Variable.soundDir, name) # tạo đường dẫn đến file
    try:
        sound = pg.mixer.Sound(fullname) # tải file âm thanh lên
    except pg.error as message: # như cái hình ảnh
        print('Cannot load sound:', fullname)
        raise SystemExit(message)
    return sound # xuất đối tượng âm thanh cho mình sử dụng

# Hàm tô màu: ( cái này chưa biết dùng đến chỗ nào nhưng nên lưu lại)
def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b,_= color# ( các chỉ số red green blue với màu alpha )
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a)) # chuyển đổi màu

def printing(font,size,surface,color,text,position=(0,0),antialias=True):
    """In text ra màn hình ở vị trí position với màu color, kích thước size, phông chữ font và làm mượt chữ(antialias=false/true)
           Lên bề mặt surface."""
    if "." in font:
        font=os.path.join(Variable.fontDir,font)
        font=pg.font.Font(font,size)
    else:
        font = pg.font.SysFont(font,size) # Tạo phông chữ
    printingText = font.render(text,antialias,color) # Tạo text
    printingTextRect = printingText.get_rect() # Tạo khung text
    printingTextRect.center = (position)# Tạo vị trí text
    surface.blit(printingText,printingTextRect) # In text lên bề mặt

def readData():
    """ Hàm để lấy dữ liệu từ lần chơi trước."""
    Variable.playerNames.clear()
    Variable.playerMoneys.clear()
    Variable.playerID.clear()
    database.selectMoneyAndName(Variable.playerID, Variable.playerNames, Variable.playerMoneys)

def writeData(ID):
    database.changeDataMoney(ID, Variable.playerMoneys[ID-1])

def playerPosition(playerName):
    """Hàm tìm vị trí của người chơi trong file name.txt (database)"""
    for i in range(0,len(Variable.playerNames)):
        if playerName==Variable.playerNames[i]:
            return i

def playerPosition(playerName):
    """Hàm tìm vị trí của người chơi trong file name.txt"""
    for i in range(0,len(Variable.playerNames)):
        if playerName==Variable.playerNames[i]:
            return i

def fade_in(screen,picture,pos):
    clock = pg.time.Clock()
    i=0
    fadeIn=True
    while i<=255 and fadeIn:
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type==pg.MOUSEBUTTONUP or event.type==pg.KEYDOWN:
                fadeIn=None
        screen.fill((0,0,0))
        picture.set_alpha(i)
        i+=1
        screen.blit(picture, pos)
        clock.tick(60)
        pg.display.flip()
        if i==256:
            fadeIn=False
    while i >=0 and not fadeIn:
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type==pg.MOUSEBUTTONUP or event.type==pg.KEYDOWN:
                fade=None
        screen.fill((0,0,0))
        picture.set_alpha(i)
        i-=1
        screen.blit(picture, pos)
        clock.tick(60)
        pg.display.flip()
      

def cuaHangData(name):
    list=[]
    playerFileName=os.path.join(Variable.playersDir,name)
    with open(playerFileName) as f:
        text=f.readline()
        while text!='':
            text=text.replace('\n', '')
            list.append(text)
            text=f.readline()
    return list

def history(data,resultData):
    for i in range(28,len(data)):
        list=data[i].split('-',3)
        resultData[0].append(list[0])
        resultData[1].append(list[1])
        resultData[2].append(list[2])
        resultData[3].append(list[3])

def updateCuaHang(name,list):
    playerFileName=os.path.join(Variable.playersDir,name)
    f=open(playerFileName,"w")
    f.writelines(f"{list[i]}\n" for i in range(0,len(list)))
    f.close()

    
#credit for edion0/redditUser.
