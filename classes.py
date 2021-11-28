
import pygame
import os,Module,Variable,mainGame
import random,KingOfBet_LostInPokemonWorld,database
class background():
    """moveBG
       Nhập screen, image của BG, image của vạch đích, vị trí pixel vạch xuất phát cách góc trái bao nhiêu
       , vị trí vạch về đích cách góc phải bao nhiêu, biến khoảng cách để chọn tọa độ, số lượng khung hình"""
    def __init__(self, screen, image, distance):
        self.screen = screen
        self.bgImage = image   
        self.rectBGImage = self.bgImage.get_rect()       
        self.bgLeft = -1200       
        self.bgTop = 0        
        self.speedBG =  1
        self.distance = distance 
        self.quangDuong=0
        self.distance=distance
        self.vachDich=self.bgLeft+self.rectBGImage.width-1420
        self.vachXuatPhat=self.bgLeft+1420
        self.move=True
    def update(self):
        if self.quangDuong <=self.distance:
            self.move=True
            self.quangDuong += self.speedBG
            self.bgLeft -= self.speedBG
        else :
            self.move=False
    def draw(self, screen):
       self.screen.blit(self.bgImage, (self.bgLeft, self.bgTop))


class pokemon(pygame.sprite.Sprite):
    """Tạo sprite pokemon"""
    def __init__(self, name,numberOfImage,pos_x=0, pos_y=0):
        super().__init__()
        self.sprites = []
        self.name=name
        folder=os.path.join(Variable.pokemonDir,name)
        for i in range(0,numberOfImage):
            image,rect=Module.load_image(f'{i}.png',folder)
            self.sprites.append(image)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.top =pos_y
        self.rect.left=pos_x
        self.rectMove=False
        self.stunOrBoot=''
        self.distance=0
        self.hieuUng=''
        self.home=0
        self.stuntime=0
        self.spriteSpeed=0.2
        self.slowtime=0
        
    def update(self,BGMoveOrNot=False):
        if self.rectMove==True:
            if self.stunOrBoot=='stun':
                if BGMoveOrNot:
                    self.rect.left-=1
                self.current_sprite -= self.spriteSpeed
                self.stuntime=self.stuntime+1
                if self.stuntime==100:
                    self.stunOrBoot=''
                    self.stuntime=0
                    self.rectMove=False
            elif self.stunOrBoot=='home':
                self.rect.left+=1
                self.distance+=1
                if self.distance>300:
                    self.distance=0
                    self.rectMove=False
                    self.stunOrBoot=''
            elif self.stunOrBoot=='boot':
                self.rect.left+=2
                self.distance+=2
                if self.distance==126:
                    self.stunOrBoot=''
                    self.rectMove=False
                    self.distance=0
            elif self.stunOrBoot=='slow':
                if BGMoveOrNot:
                    self.rect.left-=1
                self.slowtime+=1
                if self.slowtime==150:
                    self.spriteSpeed=0.2
                    self.stunOrBoot=''
                    self.slowtime=0
                    self.rectMove=False
            elif self.stunOrBoot=='reverse':
                self.distance+=1
                self.rect.left-=1
                if self.distance==150:
                    self.stunOrBoot=''
                    self.rectMove=False
                    self.distance=0
        self.current_sprite += self.spriteSpeed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        if self.stunOrBoot=='reverse':
            self.image=pygame.transform.flip(self.sprites[int(self.current_sprite)], True, False)
        else:
            self.image = self.sprites[int(self.current_sprite)]
    def bua(self,hieuUng):
        self.hieuUng=random.choice(Variable.hieuUngs)
        if hieuUng==3:
            self.rectMove=True
            self.stunOrBoot='home'
        if hieuUng==4:
            self.rect.left+=150
        if hieuUng==2 :
            self.rectMove=True
            self.stunOrBoot='stun'
        if hieuUng==1:
            self.rectMove=True    
            self.stunOrBoot='boot'
        if hieuUng==5:
            self.rectMove=True
            self.stunOrBoot='slow'
        if hieuUng==6:
            self.rect.left-=150
        if hieuUng==7:
            self.rectMove=True
            self.stunOrBoot='reverse'

