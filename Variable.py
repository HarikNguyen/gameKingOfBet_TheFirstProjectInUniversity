# -*- coding: utf-8 -*-

import os , sys

# Tạo các đường dẫn đễn file dữ liệu:
mainDir = os.path.split(os.path.abspath(__file__))[0]
dataDir = os.path.join(mainDir, "data")
fontDir=os.path.join(dataDir, "font")
imageDir=os.path.join(dataDir, "image")
soundDir=os.path.join(dataDir, "sound")
playersDir=os.path.join(dataDir,"players")
pokemonDir=os.path.join(imageDir,"pokemon")

# Khai báo biến màu:
nenToiFont=(237, 235, 228)
nenSangFont=(56, 56, 54)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE= (0, 0, 255)
RED= (200, 0, 0 )
LIGHTRED= (255, 100, 100)
PURPLE = (102, 0, 102)
LIGHTPURPLE= (153, 0, 153)
YELLOW=(255,255,0)
BLACK=(0,0,0)
CYAN=(0,255,255)
color=[WHITE,BLACK,LIGHTGREEN,GREEN,BLUE,LIGHTBLUE,LIGHTPURPLE,PURPLE,YELLOW,RED,LIGHTRED,CYAN]

# Biến khung hình:
windowWidth=1366   # Chiều rộng cửa sổ game.
windowHeight=768 # Chiều cao cửa sổ game.
newWidth=None
# Biến chuột:
x_mouse=0
y_mouse=0

# Thông tin người chơi:
playerNames=[]
playerMoneys=[]
playerID=[]

#minigame3
REVEALSPEED = 6 # speed boxes' sliding reveals and covers
BOXHEIGHT = 302 # size of box height & width in pixels
BOXWIDTH=203
GAPSIZE = 2.5 # size of gap between boxes in pixels
BOARDWIDTH = 5 # number of columns of icons
BOARDHEIGHT = 2 # number of rows of icons
XMARGIN = 45
YMARGIN = 127
FPSCLOCK=None
mousex = 0 
mousey = 0 

#mainGame:
hieuUngs=[1,2,3,4]
muteOrNot=False
