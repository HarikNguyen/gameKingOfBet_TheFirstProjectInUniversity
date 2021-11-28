import os, sys, random ,time , Module, Variable,classes
import pygame as pg
import KingOfBet_LostInPokemonWorld
import miniGame1,miniGame2,miniGame3,database

def  minigame(ID,playerName,Money) :
    """ Gọi khi người chơi muốn chơi minigame."""   
     #minigame:
    goldBoard_image,goldBoard_rect=Module.load_image("goldBoard.png","logIn")
    goldBoard_rect.center=(1150,100)
    bieuTuongGame1_image,bieuTuongGame1_rect=Module.load_image("bieuTuongGame1.png","miniGame")
    bieuTuongGame2_image,bieuTuongGame2_rect=Module.load_image("bieuTuongGame2.png","miniGame")
    bieuTuongGame3_image,bieuTuongGame3_rect=Module.load_image("bieuTuongGame3.png","miniGame")
    randomGame_image,randomGame_rect=Module.load_image("randomGame.png","miniGame")
    miniGameSelection_image,miniGameSelection_rect=Module.load_image("miniGameSelection.png","miniGame")
    quayTroLai_image,quayTroLai_rect=Module.load_image("quayTroLai.png","logIn")
    quayTroLai_rect.center=(1100,650)
    bieuTuongGame1_rect.center=(200,390)
    bieuTuongGame2_rect.center=(520,390)
    bieuTuongGame3_rect.center=(840,390)
    randomGame_rect.center=(1160,390)
    nut='no'
    pg.display.flip()
    while True:
        KingOfBet_LostInPokemonWorld.screen.blit(miniGameSelection_image,(0,0))
        KingOfBet_LostInPokemonWorld.screen.blit(goldBoard_image,goldBoard_rect)
        Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,str(Money),(1120,100))
        KingOfBet_LostInPokemonWorld.screen.blit(quayTroLai_image,quayTroLai_rect)
        KingOfBet_LostInPokemonWorld.screen.blit(bieuTuongGame1_image,bieuTuongGame1_rect)
        KingOfBet_LostInPokemonWorld.screen.blit(bieuTuongGame2_image,bieuTuongGame2_rect)
        KingOfBet_LostInPokemonWorld.screen.blit(bieuTuongGame3_image,bieuTuongGame3_rect)
        KingOfBet_LostInPokemonWorld.screen.blit(randomGame_image,randomGame_rect)
        x_mouse,y_mouse=pg.mouse.get_pos()
        if quayTroLai_rect.collidepoint(x_mouse,y_mouse) :
            nut='yes'
        else:
            nut='no'
        if nut=='yes':
            KingOfBet_LostInPokemonWorld.screen.blit(pg.transform.scale(quayTroLai_image,(quayTroLai_rect.width+10,quayTroLai_rect.height+10)),quayTroLai_rect)
        else:
            KingOfBet_LostInPokemonWorld.screen.blit(quayTroLai_image,quayTroLai_rect)
        KingOfBet_LostInPokemonWorld.clock.tick(60)
        pg.display.flip()
        current_time=pg.time.get_ticks()
        for event in pg.event.get():
            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if pg.mouse.get_pressed():
                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                    x_mouse,y_mouse=pg.mouse.get_pos()
                if quayTroLai_rect.collidepoint(x_mouse,y_mouse):
                    KingOfBet_LostInPokemonWorld.main(ID,playerName,Money)
                if bieuTuongGame1_rect.collidepoint(x_mouse,y_mouse):
                    KingOfBet_LostInPokemonWorld.channel1.fadeout(1000)
                    KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                    KingOfBet_LostInPokemonWorld.channel2.play(KingOfBet_LostInPokemonWorld.minigame1Sound,-1)
                    miniGame1.miniGame1(ID,playerName,Money)
                if bieuTuongGame2_rect.collidepoint(x_mouse,y_mouse):
                    KingOfBet_LostInPokemonWorld.channel1.fadeout(1000)
                    KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                    KingOfBet_LostInPokemonWorld.channel2.play(KingOfBet_LostInPokemonWorld.minigame2Sound, -1)
                    miniGame2.miniGame2(ID,playerName,Money)
                if bieuTuongGame3_rect.collidepoint(x_mouse,y_mouse):
                    KingOfBet_LostInPokemonWorld.channel1.fadeout(1000)
                    KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                    KingOfBet_LostInPokemonWorld.channel2.play(KingOfBet_LostInPokemonWorld.minigame3Sound, -1)
                    miniGame3.miniGame3(ID,playerName,Money)
                if randomGame_rect.collidepoint(x_mouse,y_mouse):
                    randomGame=random.randint(1,4)
                    if randomGame==1:
                        KingOfBet_LostInPokemonWorld.channel1.fadeout(1000)
                        KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                        KingOfBet_LostInPokemonWorld.channel2.play(KingOfBet_LostInPokemonWorld.minigame1Sound, -1)
                        miniGame1.miniGame1(ID,playerName,Money)
                    elif randomGame==2:
                        KingOfBet_LostInPokemonWorld.channel1.fadeout(1000)
                        KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                        KingOfBet_LostInPokemonWorld.channel2.play(KingOfBet_LostInPokemonWorld.minigame2Sound, -1)
                        miniGame2.miniGame2(ID,playerName,Money)
                    else:
                        KingOfBet_LostInPokemonWorld.channel1.fadeout(1000)
                        KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                        KingOfBet_LostInPokemonWorld.channel2.play(KingOfBet_LostInPokemonWorld.minigame3Sound, -1)
                        miniGame3.miniGame3(ID,playerName,Money)


