    # -*- coding: utf-8 -*-

import os, sys, random ,time , Module, Variable,classes
import pygame as pg
import KingOfBet_LostInPokemonWorld,Module,database
from varname import nameof

def mainGame(ID,playerName,Money):
    loading=classes.pokemon('loading',10)
    loading.spriteSpeed=0.5
    loading.rect.center=(600,550)
    mainGameBG_image,mainGameBG_rect =Module.load_image("mainBackground.png","logIn")
    def loadingTime(loading,mainGameBG_image):
        KingOfBet_LostInPokemonWorld.screen.blit(mainGameBG_image,(0,0))
        KingOfBet_LostInPokemonWorld.screen.blit(loading.image,loading.rect)
        loading.rect = loading.image.get_rect()
        loading.rect.center=(600,550)
        loading.update()
        pg.display.flip()
    betHistory=[]
    betMoney=[]
    betName=[]
    betResult=[]
    predictionResult=[]
    loadingTime(loading,mainGameBG_image)
    resultData=[]
    resultData.extend((betName,betMoney,betResult,predictionResult))
    clock = pg.time.Clock()
    step=[2,1,3,3,3,3,1,2,2,1,1]
    loadingTime(loading,mainGameBG_image)
    #Khởi tạo hình ảnh:
    plant_image,plant_rect =Module.load_image("plant.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    plant4_image,plant4_rect =Module.load_image("plant4.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    plant5_image,plant5_rect =Module.load_image("plant5.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    earth_image,earth_rect =Module.load_image("earth.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    earth4_image,earth4_rect =Module.load_image("earth4.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    earth5_image,earth5_rect =Module.load_image("earth5.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    fire_image,fire_rect =Module.load_image("fire.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    fire4_image,fire4_rect =Module.load_image("fire4.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    fire5_image,fire5_rect =Module.load_image("fire5.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    ice_image,ice_rect =Module.load_image("ice.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    ice4_image,ice4_rect =Module.load_image("ice4.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    ice5_image,ice5_rect =Module.load_image("ice5.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    finalMap_image,finalMap_rect=Module.load_image("finalMap.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    finalMap4_image,finalMap4_rect=Module.load_image("finalMap4.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    finalMap5_image,finalMap5_rect=Module.load_image("finalMap5.png","mainGame")
    loadingTime(loading,mainGameBG_image)
        #bùa:
    boot_image,boot_rect =Module.load_image("boot.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    stun_image,stun_rect =Module.load_image("stun.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    returnHome_image,returnHome_rect =Module.load_image("returnHome.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    forward_image,forward_rect =Module.load_image("forward.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    slow_image,slow_rect=Module.load_image("slow.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    backward_image,backward_rect=Module.load_image("backward.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    reverse_image,reverse_rect=Module.load_image("reverse.png","maingame")
    loadingTime(loading,mainGameBG_image)
    win_image,win_rect=Module.load_image("buaWin.png",'maingame')
    loadingTime(loading,mainGameBG_image)
    buaType=[boot_image,stun_image,returnHome_image,forward_image,slow_image,backward_image,reverse_image,win_image]
    bua_rect=[boot_rect,stun_rect,returnHome_rect,forward_rect,slow_rect,backward_rect,reverse_rect,win_rect]
    loadingTime(loading,mainGameBG_image)
        #selections
    characterSelection_image,characterSnexelection_rect =Module.load_image("charSelection.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    mapSelection_image,mapSelection_rect =Module.load_image("mapSelection.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    return_image,return_rect =Module.load_image("return.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    next_image,next_rect =Module.load_image("next.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    quit_image,quit_rect=Module.load_image("quit.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    retry_image,retry_rect=Module.load_image("retry.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    logoPlant_image,logoPlant_rect =Module.load_image("logoPlant.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    logoEarth_image,logoEarth_rect =Module.load_image("logoEarth.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    logoFire_image,logoFire_rect =Module.load_image("logoFire.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    logoIce_image,logoIce_rect =Module.load_image("logoIce.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    logoFinal_image,logoFinal_rect =Module.load_image("logoFinal.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    betBoard_image,betBoard_rect=Module.load_image("betBoard.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    betBoardBlank_image,betBoardBlank_rect=Module.load_image("betBoardBlank.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    enterMoney_image,enterMoney_rect=Module.load_image("enterMoney.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    bettingHistory_image,bettingHistory_rect=Module.load_image("bettingHistory.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    endResult_image,endResult_rect=Module.load_image("endResult.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    moneyNotification_image,moneyNotification_rect=Module.load_image("moneyNotification.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    predictionBoard_image,predictionBoard_rect=Module.load_image("predictionBoard.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    first_image,first_rect=Module.load_image("1st.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    podium_image,podium_rect=Module.load_image("podium.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    history_image,history_rect=Module.load_image("history.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    lengthSelection_image,lengthSelection_rect=Module.load_image("lengthSelection.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    startIntro_image,startIntro_rect=Module.load_image("startIntro.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    win1_image,win1_rect=Module.load_image("win.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    lose_image,lose_rect=Module.load_image("lose.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    finalSelection_image,finalSelection_rect=Module.load_image("finalSelection.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    door_image,door_rect=Module.load_image("door.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    DKhoa_image,DKhoa_rect=Module.load_image("DKhoa.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    QKhoa_image,QKhoa_rect=Module.load_image("QKhoa.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    NKhanh_image,NKhanh_rect=Module.load_image("NKhanh.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    TKhanh_image,TKhanh_rect=Module.load_image("TKhanh.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    TKhai_image,TKhai_rect=Module.load_image("TKhai.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    goldBoard_image,goldBoard_rect=Module.load_image("goldBoard.png","logIn")
    loadingTime(loading,mainGameBG_image)
    goldBoard_rect.center=(700,370)
    menuBoard_image,menuBoard_rect=Module.load_image("menuBoard.png","mainGame")
    menuBoard_rect.center=(650,400)
    mute_image,mute_rect=Module.load_image("mute.png","mainGame")
    mute_rect.center=(650,300)
    unMute_image,unMute_rect=Module.load_image("unMute.png","mainGame")
    unMute_rect.center=(650,300)
    loadingTime(loading,mainGameBG_image)
    quitOption_image,quitOption_rect=Module.load_image("quitOption.png","mainGame")
    quitOption_rect.center=(650,400)
    menu_image,menu_rect=Module.load_image("menu.png","mainGame")
    menu_rect.center=(70,40)
    x_image,x_rect=Module.load_image("x.png","mainGame")
    x_rect.center=(menuBoard_rect.left+menuBoard_rect.width-75,menuBoard_rect.top+45)
    loadingTime(loading,mainGameBG_image)
    anh=[DKhoa_image,QKhoa_image,NKhanh_image,TKhanh_image,TKhai_image]
    anh_rect=[DKhoa_rect,QKhoa_rect,NKhanh_rect,TKhanh_rect,TKhai_rect]
    return_rect.center=(80,400)
    light=classes.pokemon('light',13)
    loadingTime(loading,mainGameBG_image)
    flower=classes.pokemon('flower',46)
    loadingTime(loading,mainGameBG_image)
    fireBurn=classes.pokemon("fireBurn",4)
    loadingTime(loading,mainGameBG_image)
    fountain=classes.pokemon('fountainValley',3)
    loadingTime(loading,mainGameBG_image)
        #Maps:
    plantMap=classes.background(KingOfBet_LostInPokemonWorld.screen,plant_image,3200)
    loadingTime(loading,mainGameBG_image)
    plant4Map=classes.background(KingOfBet_LostInPokemonWorld.screen,plant4_image,4560)
    loadingTime(loading,mainGameBG_image)
    plant5Map=classes.background(KingOfBet_LostInPokemonWorld.screen,plant5_image,5920)
    loadingTime(loading,mainGameBG_image)
    earthMap=classes.background(KingOfBet_LostInPokemonWorld.screen,earth_image,3200,)
    loadingTime(loading,mainGameBG_image)
    earth4Map=classes.background(KingOfBet_LostInPokemonWorld.screen,earth4_image,4560)
    loadingTime(loading,mainGameBG_image)
    earth5Map=classes.background(KingOfBet_LostInPokemonWorld.screen,earth5_image,5920)
    loadingTime(loading,mainGameBG_image)
    fireMap=classes.background(KingOfBet_LostInPokemonWorld.screen,fire_image,3200)
    loadingTime(loading,mainGameBG_image)
    fire4Map=classes.background(KingOfBet_LostInPokemonWorld.screen,fire4_image,4560)
    loadingTime(loading,mainGameBG_image)
    fire5Map=classes.background(KingOfBet_LostInPokemonWorld.screen,fire5_image,5920)
    loadingTime(loading,mainGameBG_image)
    iceMap=classes.background(KingOfBet_LostInPokemonWorld.screen,ice_image,3200)
    loadingTime(loading,mainGameBG_image)
    ice4Map=classes.background(KingOfBet_LostInPokemonWorld.screen,ice4_image,4560)
    loadingTime(loading,mainGameBG_image)
    ice5Map=classes.background(KingOfBet_LostInPokemonWorld.screen,ice5_image,5920)
    loadingTime(loading,mainGameBG_image)
    finalMap=classes.background(KingOfBet_LostInPokemonWorld.screen,finalMap_image,3200)
    loadingTime(loading,mainGameBG_image)
    finalMap4=classes.background(KingOfBet_LostInPokemonWorld.screen,finalMap4_image,4560)
    loadingTime(loading,mainGameBG_image)
    finalMap5=classes.background(KingOfBet_LostInPokemonWorld.screen,finalMap5_image,5920)
    loadingTime(loading,mainGameBG_image)
    three=[plantMap,earthMap,fireMap,iceMap,finalMap]
    four=[plant4Map,earth4Map,fire4Map,ice4Map,finalMap4]
    five=[plant5Map,earth5Map,fire5Map,ice5Map,finalMap5]
    maps=[three,four,five]
    loadingTime(loading,mainGameBG_image)
        #Pokemons:
    #tạo pokemon:
        #plant:
    banLa = classes.pokemon('banLa',5)
    loadingTime(loading,mainGameBG_image)
    bayleef = classes.pokemon('bayleef',5)
    loadingTime(loading,mainGameBG_image)
    grottle = classes.pokemon('grottle',6)
    loadingTime(loading,mainGameBG_image)
    snivy = classes.pokemon('snivy',7)
    loadingTime(loading,mainGameBG_image)
    hoaTrenDau=classes.pokemon('hoaTrenDau',3)
    loadingTime(loading,mainGameBG_image)
    plantPokemons = pg.sprite.Group()
    loadingTime(loading,mainGameBG_image)
    plantPokemons.add(banLa,bayleef,grottle,snivy,hoaTrenDau)
    loadingTime(loading,mainGameBG_image)
    banLa_anmung = classes.pokemon('banLa_anmung',5)
    loadingTime(loading,mainGameBG_image)
    bayleef_anmung = classes.pokemon('bayleef_anmung',4)
    loadingTime(loading,mainGameBG_image)
    grottle_anmung = classes.pokemon('grottle_anmung',4)
    loadingTime(loading,mainGameBG_image)
    snivy_anmung = classes.pokemon('snivy_anmung',6)
    loadingTime(loading,mainGameBG_image)
    hoaTrenDau_anmung=classes.pokemon('hoaTrenDau_anmung',5)
    loadingTime(loading,mainGameBG_image)
    plantPokemons_anmung = pg.sprite.Group()
    loadingTime(loading,mainGameBG_image)
    plantPokemons_anmung.add(banLa_anmung,bayleef_anmung,grottle_anmung,snivy_anmung,hoaTrenDau_anmung)
    bayleefSound=Module.load_sound("bayleef.mp3")
    loadingTime(loading,mainGameBG_image)
    grotleSound=Module.load_sound("grotle.mp3")
    loadingTime(loading,mainGameBG_image)
    snivySound=Module.load_sound("snivy.mp3")
    loadingTime(loading,mainGameBG_image)
    plantSound=[bayleefSound,grotleSound,snivySound]
        #earth:
    earthBear = classes.pokemon('earthBear',10)
    loadingTime(loading,mainGameBG_image)
    mareep = classes.pokemon('mareep',4)
    loadingTime(loading,mainGameBG_image)
    zoroak = classes.pokemon('zoroak',4)
    loadingTime(loading,mainGameBG_image)
    umbreon = classes.pokemon('umbreon',5)
    loadingTime(loading,mainGameBG_image)
    lacDa=classes.pokemon('lacDa',5)
    loadingTime(loading,mainGameBG_image)
    earthPokemons = pg.sprite.Group()
    earthPokemons.add(earthBear,mareep,zoroak,umbreon,lacDa)
    earthBear_anmung = classes.pokemon('earthBear_anmung',7)
    loadingTime(loading,mainGameBG_image)
    mareep_anmung = classes.pokemon('mareep_anmung',3)
    loadingTime(loading,mainGameBG_image)
    zoroak_anmung = classes.pokemon('zoroak_anmung',3)
    loadingTime(loading,mainGameBG_image)
    umbreon_anmung = classes.pokemon('umbreon_anmung',4)
    loadingTime(loading,mainGameBG_image)
    lacDa_anmung=classes.pokemon('lacDa_anmung',4)
    loadingTime(loading,mainGameBG_image)
    earthPokemons_anmung = pg.sprite.Group()
    earthPokemons_anmung.add(earthBear_anmung,mareep_anmung,zoroak_anmung,umbreon_anmung,lacDa_anmung)
    mareepSound=Module.load_sound("mareep.mp3")
    loadingTime(loading,mainGameBG_image)
    zoroakSound=Module.load_sound("zoroark.mp3")
    loadingTime(loading,mainGameBG_image)
    earthSound=[mareepSound,zoroakSound]
        #fire:
    fireMouse = classes.pokemon('fireMouse',6)
    loadingTime(loading,mainGameBG_image)
    monferno = classes.pokemon('monferno',6)
    loadingTime(loading,mainGameBG_image)
    pansear = classes.pokemon('pansear',6)
    loadingTime(loading,mainGameBG_image)
    houndour = classes.pokemon('houndour',7)
    loadingTime(loading,mainGameBG_image)
    gaLua=classes.pokemon('gaLua',6)
    firePokemons = pg.sprite.Group()
    firePokemons.add(fireMouse,monferno,pansear,houndour,gaLua)
    loadingTime(loading,mainGameBG_image)
    fireMouse_anmung = classes.pokemon('fireMouse_anmung',6)
    loadingTime(loading,mainGameBG_image)
    monferno_anmung = classes.pokemon('monferno_anmung',5)
    loadingTime(loading,mainGameBG_image)
    pansear_anmung = classes.pokemon('pansear_anmung',5)
    loadingTime(loading,mainGameBG_image)
    houndour_anmung = classes.pokemon('houndour_anmung',3)
    loadingTime(loading,mainGameBG_image)
    gaLua_anmung=classes.pokemon('gaLua_anmung',5)
    loadingTime(loading,mainGameBG_image)
    firePokemons_anmung = pg.sprite.Group()
    firePokemons_anmung.add(fireMouse_anmung,monferno_anmung,pansear_anmung,houndour_anmung,gaLua_anmung)
    monfernoSound=Module.load_sound("monferno.mp3")
    loadingTime(loading,mainGameBG_image)
    pansearSound=Module.load_sound("pansear.mp3")
    houndourSound=Module.load_sound("houndour.mp3")
    fireSound=[monfernoSound,pansearSound,houndourSound]
    loadingTime(loading,mainGameBG_image)
        #ice:
    panpour = classes.pokemon('panpour',6)
    loadingTime(loading,mainGameBG_image)
    marshtomp = classes.pokemon('marshtomp',8)
    loadingTime(loading,mainGameBG_image)
    prinplup = classes.pokemon('prinplup',4)
    loadingTime(loading,mainGameBG_image)
    waterCro = classes.pokemon('waterCro',8)
    loadingTime(loading,mainGameBG_image)
    caVoi=classes.pokemon('caVoi',7)
    icePokemons = pg.sprite.Group()
    icePokemons.add(panpour,marshtomp,prinplup,waterCro,caVoi)
    panpour_anmung = classes.pokemon('panpour_anmung',5)
    loadingTime(loading,mainGameBG_image)
    marshtomp_anmung = classes.pokemon('marshtomp_anmung',4)
    loadingTime(loading,mainGameBG_image)
    prinplup_anmung = classes.pokemon('prinplup_anmung',4)
    loadingTime(loading,mainGameBG_image)
    waterCro_anmung = classes.pokemon('waterCro_anmung',4)
    loadingTime(loading,mainGameBG_image)
    caVoi_anmung=classes.pokemon('caVoi_anmung',6)
    loadingTime(loading,mainGameBG_image)
    icePokemons_anmung = pg.sprite.Group()
    icePokemons_anmung.add(panpour_anmung,marshtomp_anmung,prinplup_anmung,waterCro_anmung,caVoi_anmung)
    panpourSound=Module.load_sound("panpour.mp3")
    marshtompSound=Module.load_sound("marshtomp.mp3")
    prinplupSound=Module.load_sound("prinplup.mp3")
    iceSound=[panpourSound,marshtompSound,prinplupSound]
    loadingTime(loading,mainGameBG_image)
        #final:
    NKhanh=classes.pokemon('NKhanh',5)
    loadingTime(loading,mainGameBG_image)
    QKhoa=classes.pokemon('QKhoa',5)
    loadingTime(loading,mainGameBG_image)
    DKhoa=classes.pokemon('DKhoa',5)
    loadingTime(loading,mainGameBG_image)
    TKhanh=classes.pokemon('TKhanh',5)
    loadingTime(loading,mainGameBG_image)
    TKhai=classes.pokemon('TKhai',5)
    loadingTime(loading,mainGameBG_image)
    NKhanh_anmung=classes.pokemon('NKhanh_anmung',5)
    loadingTime(loading,mainGameBG_image)
    QKhoa_anmung=classes.pokemon('QKhoa_anmung',5)
    loadingTime(loading,mainGameBG_image)
    DKhoa_anmung=classes.pokemon('DKhoa_anmung',5)
    loadingTime(loading,mainGameBG_image)
    TKhanh_anmung=classes.pokemon('TKhanh_anmung',5)
    loadingTime(loading,mainGameBG_image)
    TKhai_anmung=classes.pokemon('TKhai_anmung',5)
    loadingTime(loading,mainGameBG_image)
    finalSprite = pg.sprite.Group()
    finalSprite.add(DKhoa,QKhoa,NKhanh,TKhanh,TKhai)
    finalSprite_anmung = pg.sprite.Group()
    finalSprite_anmung.add(DKhoa_anmung,QKhoa_anmung,NKhanh_anmung,TKhanh_anmung,TKhai_anmung)
    # Cỗ vũ:
    polarBear=classes.pokemon('polarBear', 27)
    loadingTime(loading,mainGameBG_image)
    yellowCrewmate=classes.pokemon('yellowCrewmate',26)
    loadingTime(loading,mainGameBG_image)
    redCrewmate=classes.pokemon('redCrewmate',19)  
    loadingTime(loading,mainGameBG_image) 
    blueCrewmate=classes.pokemon('blueCrewmate',17)
    loadingTime(loading,mainGameBG_image)
    shark=classes.pokemon('shark',23)
    loadingTime(loading,mainGameBG_image)
    penguin=classes.pokemon('penguin',18)
    loadingTime(loading,mainGameBG_image)
    narancia=classes.pokemon('narancia',27)
    loadingTime(loading,mainGameBG_image)
    girl=classes.pokemon('girl',15)
    loadingTime(loading,mainGameBG_image)
    cheem=classes.pokemon('cheem',8)
    loadingTime(loading,mainGameBG_image)
    # tạo list pokemon:
    pokemonList=[plantPokemons,earthPokemons,firePokemons,icePokemons,finalSprite]
    anMungList=[plantPokemons_anmung,earthPokemons_anmung,firePokemons_anmung,icePokemons_anmung,finalSprite_anmung]
    stunEffect=classes.pokemon('stunEffect',9)
    loadingTime(loading,mainGameBG_image)
    bootEffect=classes.pokemon('bootEffect',6)
    loadingTime(loading,mainGameBG_image)
    slowEffect=classes.pokemon('slowEffect',6)
    loadingTime(loading,mainGameBG_image)
    reverseEffect=classes.pokemon('reverse',3)
    loadingTime(loading,mainGameBG_image)
    forwardEffect=classes.pokemon('forward',5)
    loadingTime(loading,mainGameBG_image)
    backwardEffect=classes.pokemon('backward',6)
    loadingTime(loading,mainGameBG_image)
    slowEffect.spriteSpeed=0.25
    data=Module.cuaHangData(playerName)
    playerCoVu=[blueCrewmate,shark,narancia,redCrewmate,penguin,polarBear,cheem,yellowCrewmate,girl]
    coVu_pos=[(300,110),(600,110),(900,100),(1200,110),(1500,110),(1800,110),(2100,110),(2400,110),(2700,110),(3000,110)]
    for i in range(0,len(playerCoVu)):
        playerCoVu[i].rect.center=coVu_pos[i]
    line=[200,320,440,550,670]
    gametime=pg.time.get_ticks()
    loadingTime(loading,mainGameBG_image)
    chooseMap=None
    total=0
    choosePokemon=None
    loadingTime(loading,mainGameBG_image)
    bet=None
    play=None
    result=None
    prediction=None
    cameras=['No','No','No','No','No']
    loadingTime(loading,mainGameBG_image)
    mapLength=None
    instruction_image,instruction_rect=Module.load_image("instruction.png","mainGame")
    instruction_rect.center=(650,400)
    xButton_image,xButton_rect=Module.load_image("xButton.png","mainGame")
    loadingTime(loading,mainGameBG_image)
    xButton_rect.center=(1050,150)
    three_rect=pg.Rect(253,320,218,192)
    four_rect=pg.Rect(500,320,273,192)
    five_rect=pg.Rect(801,320,327,192)
    loadingTime(loading,mainGameBG_image)
    logoPlant_rect.top=192
    logoPlant_rect.left=237
    logoEarth_rect.top=192
    logoEarth_rect.left=845
    loadingTime(loading,mainGameBG_image)
    logoFire_rect.top=524
    logoFire_rect.left=236
    logoIce_rect.top=524
    logoIce_rect.left=845
    logoFinal_rect.top=345
    loadingTime(loading,mainGameBG_image)
    logoFinal_rect.left=585
    lengthRect=[three_rect,four_rect,five_rect]
    loadingTime(loading,mainGameBG_image)
    chooseLength=0
    return_rect.center=(80,400)
    KingOfBet_LostInPokemonWorld.screen.fill((255,198,64))
    KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
    KingOfBet_LostInPokemonWorld.screen.blit(lengthSelection_image,lengthSelection_rect)
    pg.display.flip()
    while True:
        # Chọn độ dài:
        if chooseLength==0:
            KingOfBet_LostInPokemonWorld.screen.fill((255,198,64))
            KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(lengthSelection_image,lengthSelection_rect)
            pg.display.flip()
            pickLength=True
            while pickLength:
                for event in pg.event.get():
                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONUP:
                        if pg.mouse.get_pressed():
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                            mouseX,mouseY=pg.mouse.get_pos()# chỗ này chọn map
                            for rect in range (0,len(lengthRect)):
                                if lengthRect[rect].collidepoint(mouseX,mouseY):
                                    mapLength=rect
                                    pickLength=False
                                    chooseLength=2
                                    chooseMap=0
                        if return_rect.collidepoint(mouseX,mouseY):
                                KingOfBet_LostInPokemonWorld.channel2.fadeout(1000)
                                KingOfBet_LostInPokemonWorld.main(ID,playerName,Money)
        #Chọn map
        if chooseMap==0:
            KingOfBet_LostInPokemonWorld.screen.blit(mapSelection_image,(0,-5))
            return_rect.center=(80,400)
            KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(logoPlant_image,logoPlant_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(logoEarth_image,logoEarth_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(logoFire_image,logoFire_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(logoIce_image,logoIce_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(logoFinal_image,logoFinal_rect)
            pg.display.flip()
            pickMap=True
            while pickMap:
                for event in pg.event.get():
                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONUP:
                        if pg.mouse.get_pressed():
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                            mouseX,mouseY=pg.mouse.get_pos()# chỗ này chọn map
                            if logoPlant_rect.collidepoint(mouseX,mouseY):
                                map=0
                                anmung=anMungList[map].sprites()
                                maps[mapLength][map].bgLeft=-1200
                                maps[mapLength][map].bgTop = 0
                                maps[mapLength][map].quangDuong = 0
                                maps[mapLength][map].move=True
                                maps[mapLength][map].vachDich=maps[mapLength][map].bgLeft+maps[mapLength][map].rectBGImage.width-1420
                                maps[mapLength][map].vachXuatPhat=maps[mapLength][map].bgLeft+1420
                                pokemons=pokemonList[map].sprites()
                                pickMap=False
                                chooseMap=1
                            elif return_rect.collidepoint(mouseX,mouseY):
                                pickMap=False
                                choosemap=1
                                chooseLength=0
                            elif logoEarth_rect.collidepoint(mouseX,mouseY):
                                map=1
                                chooseMap=1
                                maps[mapLength][map].bgTop = 0
                                maps[mapLength][map].bgLeft=-1200
                                maps[mapLength][map].quangDuong = 0
                                maps[mapLength][map].move=True
                                maps[mapLength][map].vachDich=maps[mapLength][map].bgLeft+maps[mapLength][map].rectBGImage.width-1420
                                maps[mapLength][map].vachXuatPhat=maps[mapLength][map].bgLeft+1420
                                pokemons=pokemonList[map].sprites()
                                anmung=anMungList[map].sprites()
                                pickMap=False
                            elif logoFire_rect.collidepoint(mouseX,mouseY):
                                map=2
                                pokemons=pokemonList[map].sprites()
                                anmung=anMungList[map].sprites()
                                chooseMap=1
                                maps[mapLength][map].bgTop = 0
                                maps[mapLength][map].bgLeft=-1200
                                maps[mapLength][map].quangDuong = 0
                                maps[mapLength][map].move=True
                                maps[mapLength][map].vachDich=maps[mapLength][map].bgLeft+maps[mapLength][map].rectBGImage.width-1420
                                maps[mapLength][map].vachXuatPhat=maps[mapLength][map].bgLeft+1420
                                pickMap=False
                            elif logoIce_rect.collidepoint(mouseX,mouseY):
                                map=3
                                maps[mapLength][map].bgTop = 0
                                maps[mapLength][map].bgLeft=-1200
                                maps[mapLength][map].quangDuong = 0
                                maps[mapLength][map].move=True
                                maps[mapLength][map].vachDich=maps[mapLength][map].bgLeft+maps[mapLength][map].rectBGImage.width-1420
                                maps[mapLength][map].vachXuatPhat=maps[mapLength][map].bgLeft+1420
                                pokemons=pokemonList[map].sprites()
                                anmung=anMungList[map].sprites()
                                pickMap=False
                                chooseMap=1
                            elif logoFinal_rect.collidepoint(mouseX,mouseY):
                                map=4
                                maps[mapLength][map].bgTop = 0
                                maps[mapLength][map].bgLeft=-1200
                                maps[mapLength][map].quangDuong = 0
                                maps[mapLength][map].move=True
                                maps[mapLength][map].vachDich=maps[mapLength][map].bgLeft+maps[mapLength][map].rectBGImage.width-1420
                                maps[mapLength][map].vachXuatPhat=maps[mapLength][map].bgLeft+1420
                                chooseMap=1
                                pokemons=pokemonList[map].sprites()
                                anmung=anMungList[map].sprites()
                                pickMap=False
            if chooseMap==1:
                choosePokemon=0
                chooseMap=2
        # Chọn pokemon:
        if choosePokemon==0:# cái này chọn pokemon
            if map!=4:
                KingOfBet_LostInPokemonWorld.screen.blit(characterSelection_image,(0,0))
                return_rect.center=(80,400)
                KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                pokemon_pos=[(400,280),(970,280),(675,450),(400,590),(970,590)]
                for i in range(0,5):
                    pokemons[i].rect.center=pokemon_pos[i]
                pokemonList[map].draw(KingOfBet_LostInPokemonWorld.screen)
                pickPokemon=True
                pg.display.flip()
                while pickPokemon:
                    KingOfBet_LostInPokemonWorld.screen.blit(characterSelection_image,(0,0))
                    KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                    pokemonList[map].draw(KingOfBet_LostInPokemonWorld.screen)
                    pokemonList[map].update(maps[mapLength][map].move)
                    for event in pg.event.get():
                        if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                            pg.display.quit()
                            pg.quit()
                            sys.exit()
                        if event.type == pg.MOUSEBUTTONUP:
                            if pg.mouse.get_pressed():
                                KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                mouseX,mouseY=pg.mouse.get_pos()
                                if pokemons[0].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=0
                                    choosePokemon=1
                                    pickPokemon=False
                                elif return_rect.collidepoint(mouseX,mouseY):
                                    choosePokemon=2
                                    chooseMap=0
                                    pickPokemon=False
                                elif  pokemons[1].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=1
                                    choosePokemon=1
                                    pickPokemon=False
                                elif  pokemons[2].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=2
                                    choosePokemon=1
                                    pickPokemon=False
                                elif  pokemons[3].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=3
                                    choosePokemon=1
                                    pickPokemon=False
                                elif pokemons[4].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=4
                                    choosePokemon=1
                                    pickPokemon=False
                    pg.display.flip()
                    clock.tick(60)
            else:
                KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                return_rect.center=(80,400)
                KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                pokemon_pos=[(240,200),(460,200),(670,200),(890,200),(1120,200)]
                for i in range(0,5):
                    pokemons[i].rect.center=pokemon_pos[i]
                anh_pos=[(240,-200),(460,-200),(670,-200),(890,-200),(1120,-200)]
                for i in range(0,5):
                    anh_rect[i].center=anh_pos[i]
                pokemonList[map].draw(KingOfBet_LostInPokemonWorld.screen)
                fireBurn.spriteSpeed=0.25
                pickPokemon=True
                pg.display.flip()
                while pickPokemon:
                    KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                    return_rect.center=(80,400)
                    KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                    pokemonList[map].draw(KingOfBet_LostInPokemonWorld.screen)
                    pokemonList[map].update(maps[mapLength][map].move)
                    for event in pg.event.get():
                        if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                            pg.display.quit()
                            pg.quit()
                            sys.exit()
                        if event.type == pg.MOUSEBUTTONUP:
                            if pg.mouse.get_pressed():
                                KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                mouseX,mouseY=pg.mouse.get_pos()
                                if pokemons[0].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=0
                                    choosePokemon=1
                                    pickPokemon=False
                                    timeWait=0
                                    while timeWait<100:
                                        for event in pg.event.get():
                                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                                pg.display.quit()
                                                pg.quit()
                                                sys.exit()
                                            if event.type == pg.MOUSEBUTTONUP:
                                                if pg.mouse.get_pressed():
                                                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    mouseX,mouseY=pg.mouse.get_pos()
                                                    if return_rect.collidepoint(mouseX,mouseY):
                                                        choosePokemon=2
                                                        chooseMap=0
                                                        pickPokemon=False  
                                        KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                                        return_rect.center=(80,400)
                                        KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                                        fireBurn.update(maps[mapLength][map].move)
                                        for i in range(0,5):
                                            if anh_rect[i].center[1]<380:
                                                anh_rect[i].top+=20
                                            KingOfBet_LostInPokemonWorld.screen.blit(anh[i],anh_rect[i])
                                            KingOfBet_LostInPokemonWorld.screen.blit(fireBurn.image,(anh_rect[i].left-20,anh_rect[i].top-20))
                                        timeWait+=1
                                        clock.tick(60)
                                        pg.display.flip()
                                elif return_rect.collidepoint(mouseX,mouseY):
                                    choosePokemon=2
                                    chooseMap=0
                                    pickPokemon=False
                                elif  pokemons[1].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=1
                                    choosePokemon=1
                                    pickPokemon=False
                                    timeWait=0
                                    while timeWait<100:
                                        for event in pg.event.get():
                                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                                pg.display.quit()
                                                pg.quit()
                                                sys.exit()
                                            if event.type == pg.MOUSEBUTTONUP:
                                                if pg.mouse.get_pressed():
                                                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    mouseX,mouseY=pg.mouse.get_pos()
                                                    if return_rect.collidepoint(mouseX,mouseY):
                                                        choosePokemon=2
                                                        chooseMap=0
                                                        pickPokemon=False  
                                        KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                                        return_rect.center=(80,400)
                                        KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                                        fireBurn.update(maps[mapLength][map].move)
                                        for i in range(0,5):
                                            if anh_rect[i].center[1]<380:
                                                anh_rect[i].top+=20
                                            KingOfBet_LostInPokemonWorld.screen.blit(anh[i],anh_rect[i])
                                            KingOfBet_LostInPokemonWorld.screen.blit(fireBurn.image,(anh_rect[i].left-20,anh_rect[i].top-20))
                                        timeWait+=1
                                        clock.tick(60)
                                        pg.display.flip()
                                elif  pokemons[2].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=2
                                    choosePokemon=1
                                    pickPokemon=False
                                    timeWait=0
                                    while timeWait<100:
                                        for event in pg.event.get():
                                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                                pg.display.quit()
                                                pg.quit()
                                                sys.exit()
                                            if event.type == pg.MOUSEBUTTONUP:
                                                if pg.mouse.get_pressed():
                                                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    mouseX,mouseY=pg.mouse.get_pos()
                                                    if return_rect.collidepoint(mouseX,mouseY):
                                                        choosePokemon=2
                                                        chooseMap=0
                                                        pickPokemon=False  
                                        KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                                        return_rect.center=(80,400)
                                        KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                                        fireBurn.update(maps[mapLength][map].move)
                                        for i in range(0,5):
                                            if anh_rect[i].center[1]<380:
                                                anh_rect[i].top+=20
                                            KingOfBet_LostInPokemonWorld.screen.blit(anh[i],anh_rect[i])
                                            KingOfBet_LostInPokemonWorld.screen.blit(fireBurn.image,(anh_rect[i].left-20,anh_rect[i].top-20))
                                        timeWait+=1
                                        clock.tick(60)
                                        pg.display.flip()
                                elif  pokemons[3].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=3
                                    choosePokemon=1
                                    pickPokemon=False
                                    timeWait=0
                                    while timeWait<100:
                                        for event in pg.event.get():
                                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                                pg.display.quit()
                                                pg.quit()
                                                sys.exit()
                                            if event.type == pg.MOUSEBUTTONUP:
                                                if pg.mouse.get_pressed():
                                                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    mouseX,mouseY=pg.mouse.get_pos()
                                                    if return_rect.collidepoint(mouseX,mouseY):
                                                        choosePokemon=2
                                                        chooseMap=0
                                                        pickPokemon=False  
                                        KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                                        return_rect.center=(80,400)
                                        KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                                        fireBurn.update(maps[mapLength][map].move)
                                        for i in range(0,5):
                                            if anh_rect[i].center[1]<380:
                                                anh_rect[i].top+=20
                                            KingOfBet_LostInPokemonWorld.screen.blit(anh[i],anh_rect[i])
                                            KingOfBet_LostInPokemonWorld.screen.blit(fireBurn.image,(anh_rect[i].left-20,anh_rect[i].top-20))
                                        timeWait+=1
                                        clock.tick(60)
                                        pg.display.flip()
                                elif pokemons[4].rect.collidepoint(mouseX,mouseY):
                                    pokemonSelection=4
                                    choosePokemon=1
                                    pickPokemon=False
                                    timeWait=0
                                    while timeWait<100:
                                        for event in pg.event.get():
                                            if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                                pg.display.quit()
                                                pg.quit()
                                                sys.exit()
                                            if event.type == pg.MOUSEBUTTONUP:
                                                if pg.mouse.get_pressed():
                                                    KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                    mouseX,mouseY=pg.mouse.get_pos()
                                                    if return_rect.collidepoint(mouseX,mouseY):
                                                        choosePokemon=2
                                                        chooseMap=0
                                                        pickPokemon=False  
                                        KingOfBet_LostInPokemonWorld.screen.blit(finalSelection_image,(0,0))
                                        return_rect.center=(80,400)
                                        KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                                        fireBurn.update(maps[mapLength][map].move)
                                        for i in range(0,5):
                                            if anh_rect[i].center[1]<380:
                                                anh_rect[i].top+=20
                                            KingOfBet_LostInPokemonWorld.screen.blit(anh[i],anh_rect[i])
                                            KingOfBet_LostInPokemonWorld.screen.blit(fireBurn.image,(anh_rect[i].left-20,anh_rect[i].top-20))
                                        timeWait+=1
                                        clock.tick(60)
                                        pg.display.flip()
                    pg.display.flip()
                    clock.tick(60)
            if choosePokemon==1:
                bet=0
                choosePokemon=2
         #đặt  tiền cược
        if bet==0:# cái này đặt cược
            return_rect.center=(80,400)
            goldBoard_rect.center=(700,370)
            betGold=''
            betGoldInt=0
            bet=1
            enterMoney_rect.center=(690,540)
            getBet=False
            KingOfBet_LostInPokemonWorld.screen.blit(betBoard_image,betBoard_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(enterMoney_image,enterMoney_rect)
            KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
            working=True
            pg.display.flip()
            while working:
                KingOfBet_LostInPokemonWorld.screen.blit(betBoardBlank_image,(559,177))
                KingOfBet_LostInPokemonWorld.screen.blit(goldBoard_image,goldBoard_rect)
                Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,str(Money),(670,370))
                pokemons[pokemonSelection].rect.center=(670,230)
                pokemons[pokemonSelection].update(maps[mapLength][map].move)
                KingOfBet_LostInPokemonWorld.screen.blit(pokemons[pokemonSelection].image,pokemons[pokemonSelection].rect)
                for event in pg.event.get():
                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONUP:
                        if pg.mouse.get_pressed():
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                            x_mouse,y_mouse=pg.mouse.get_pos()
                        if enterMoney_rect.collidepoint(x_mouse,y_mouse):
                            getBet=True
                        if return_rect.collidepoint(x_mouse,y_mouse):
                            bet==1
                            choosePokemon=0
                            working=False
                    if event.type == pg.KEYDOWN:
                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                        if getBet:
                            if event.key == pg.K_RETURN:
                                if int(betGold)>Money:
                                    Module.printing('JosefinSans-BoldItalic.ttf',50,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,'You don\'t have enough Gold',(670,370))
                                else:
                                    bet=2
                                    prediction=0
                                    betGoldInt=int(betGold)
                                    getBet=False
                                    working=False
                            elif event.key == pg.K_BACKSPACE:
                                betGold = betGold[:-1]
                                KingOfBet_LostInPokemonWorld.screen.blit(enterMoney_image,enterMoney_rect)
                                Module.printing('JosefinSans-BoldItalic.ttf',30,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,betGold,enterMoney_rect.center)
                            elif event.unicode in '0123456789':
                                betGold += event.unicode
                                KingOfBet_LostInPokemonWorld.screen.blit(enterMoney_image,enterMoney_rect)
                                Module.printing('JosefinSans-BoldItalic.ttf',30,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,betGold,enterMoney_rect.center)
                clock.tick(60)
                pg.display.flip()
        if prediction==0:# cái này dự đoán
            pos1=[(750,250),(945,250),(1135,250),(830,445),(1045,445)]
            for pokemon in range (0,len(pokemons)):
                    pokemons[pokemon].rect.center=pos1[pokemon]
            pos2=[(345,85),(345,230),(345,380),(345,525),(345,675)]
            predictionList=[None,None,None,None,None]
            KingOfBet_LostInPokemonWorld.screen.blit(predictionBoard_image,(0,0))
            return_rect.center=(1310,450)
            next_rect.center=(1310,250)
            predictionTime=True
            while predictionTime:
                KingOfBet_LostInPokemonWorld.screen.blit(predictionBoard_image,(0,0))
                KingOfBet_LostInPokemonWorld.screen.blit(return_image,return_rect)
                KingOfBet_LostInPokemonWorld.screen.blit(next_image,next_rect)
                pokemonList[map].update(maps[mapLength][map].move)
                pokemonList[map].draw(KingOfBet_LostInPokemonWorld.screen)
                clock.tick(60)
                pg.display.flip()
                for event in pg.event.get():
                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONUP:
                        if pg.mouse.get_pressed():
                            x_mouse,y_mouse=pg.mouse.get_pos()
                        if return_rect.collidepoint(x_mouse,y_mouse):
                            prediction=1
                            bet=0
                            predictionTime=False
                        if next_rect.collidepoint(x_mouse,y_mouse) and None not in predictionList:
                            prediction=2
                            predictionTime=False
                        for pokemon in range(0,len(pokemons)):
                            if pokemons[pokemon].rect.collidepoint(x_mouse,y_mouse):
                                if pokemons[pokemon].rect.center==pos1[pokemon]:
                                    for pos in range (0,len(pos2)):
                                        if predictionList[pos]==None:
                                            pokemons[pokemon].rect.center=pos2[pos]
                                            predictionList[pos]=pokemons[pokemon]
                                            break
                                else:
                                    for pos in range (0,len(pos2)):
                                        if pos2[pos]==pokemons[pokemon].rect.center:
                                            pokemons[pokemon].rect.center=pos1[pokemon]
                                            predictionList[pos]=None
                                            break
                if chooseMap==2 and choosePokemon==2 and bet==2 and prediction==2 and chooseLength==2:
                    play=0
                    pokemon_pos=[(maps[mapLength][map].vachXuatPhat,160),(maps[mapLength][map].vachXuatPhat,280),(maps[mapLength][map].vachXuatPhat,400),(maps[mapLength][map].vachXuatPhat,520),(maps[mapLength][map].vachXuatPhat,640)]
                    for i in range(0,5):
                        pokemons[i].rect.left,pokemons[i].rect.top=pokemon_pos[i]
                    moveDistance=None
                    finish=[]
                    rank=[]
                    stop=[]
                    buas=[]
                    buaPos=[]
                    buaMoves=[]
                    hieuUngs=[]
                    viTris=[]
                    cameras=['No','No','No','No','No']
                    selectDefaultCamera=0
                    startIntro=True
                    hieuUngStun=False
                    hieuUngBoot=False
                    hieuUngSlow=False
                    hieuUngForward=False
                    hieuUngBackward=False
                    hieuUngReverse=False
                    if mapLength==0:
                        fountain.rect.left=maps[mapLength][map].bgLeft+4370
                        fountain.rect.top=-50
                    elif mapLength==1:
                        fountain.rect.left=maps[mapLength][map].bgLeft+4750
                        fountain.rect.top=-50
                    else:
                        fountain.rect.left=maps[mapLength][map].bgLeft+5620
                        fountain.rect.top=-50
                    for i in range (0,25+mapLength*2):
                        viTris.append(int(maps[mapLength][map].vachDich-200-i*maps[mapLength][map].rectBGImage.width/(30+mapLength*2)))
                    for i in range(0,20+mapLength*2) :
                        if i <19:
                            hieuUng=random.choice((1,2,4,5,6,7,1,2,4,5,6,7,1,2,4,5,6,7,3))
                            viTri=random.choice(viTris)
                            viTris.remove(viTri)
                            if viTri>500:
                                buaPos.append(pg.Rect(viTri,random.choice(line),75,75))
                                hieuUngs.append(hieuUng)
                                buas.append(buaType[hieuUng-1])
                                KingOfBet_LostInPokemonWorld.screen.blit(buas[len(buas)-1],buaPos[len(buas)-1])
                                buaMoves.append(True)
                        else:
                            hieuUng=random.choice((1,2,3,4,5,6,7,1,2,3,4,1,2,3,1,2,2,3,4,5,3,2,4,5,6,1,2,2,1,2,3,4,3,4,8,8,8,8,8))
                            viTri=random.choice(viTris)
                            if viTri>500:
                                buaPos.append(pg.Rect(viTri,random.choice(line),75,75))
                                hieuUngs.append(hieuUng)
                                buas.append(buaType[hieuUng-1])
                                KingOfBet_LostInPokemonWorld.screen.blit(buas[len(buas)-1],buaPos[len(buas)-1])
                                buaMoves.append(True)
                    for i in range(0,len(coVu_pos)):
                        coVu_pos[i]=((mapLength-3)*100,110)
                    door_rect.left=maps[mapLength][map].vachXuatPhat+50
                    door_rect.top=50
                    goldBoard_rect.center=(1200,30)
                    breakpoint=pg.time.get_ticks()
                    gametime=pg.time.get_ticks()
        while play==0:# cái này bắt đầu chơi
            while data[22]=='0':
                KingOfBet_LostInPokemonWorld.screen.fill((250 ,229, 89))
                KingOfBet_LostInPokemonWorld.screen.blit(instruction_image, instruction_rect)
                KingOfBet_LostInPokemonWorld.screen.blit(xButton_image,xButton_rect)   
                pg.display.flip()
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
                                data[22]='1'
                                Module.updateCuaHang(playerName,data)
            if selectDefaultCamera==0 and 'Yes' not in cameras and maps[mapLength][map].quangDuong>600:
                selectDefaultCamera=1
                cameras[pokemonSelection]='Yes'
            if maps[mapLength][map].move:
                maps[mapLength][map].vachDich-=1
            maps[mapLength][map].update()
            maps[mapLength][map].draw(KingOfBet_LostInPokemonWorld.screen)
            num=1
            if map!=4:
                for i in range(2,len(playerCoVu)+2):
                    if data[i]=='sold':
                        playerCoVu[i-2].update( maps[mapLength][map].move)
                        if maps[mapLength][map].move:
                            playerCoVu[i-2].rect.left-=1
                        KingOfBet_LostInPokemonWorld.screen.blit(playerCoVu[i-2].image,playerCoVu[i-2].rect)
            else:
                KingOfBet_LostInPokemonWorld.screen.blit(fountain.image,fountain.rect)
                fountain.update( maps[mapLength][map].move)
                if maps[mapLength][map].move:
                    fountain.rect.left-=1
            KingOfBet_LostInPokemonWorld.screen.blit(goldBoard_image,goldBoard_rect)
            Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,str(Money),(1180,30))
            KingOfBet_LostInPokemonWorld.screen.blit(menu_image,menu_rect)
            if startIntro:
                if map==4:
                    KingOfBet_LostInPokemonWorld.screen.blit(door_image,door_rect)
                for pokemon in pokemons:
                    KingOfBet_LostInPokemonWorld.screen.blit(pokemon.image,pokemon.rect)
                KingOfBet_LostInPokemonWorld.screen.blit(startIntro_image,startIntro_rect)
                pg.display.flip()
                pg.time.wait(2000)
                if map==4:
                    while door_rect.top<770:
                        door_rect.top+=10
                        door_rect.left-=5
                        maps[mapLength][map].draw(KingOfBet_LostInPokemonWorld.screen)
                        for pokemon in pokemons:
                            KingOfBet_LostInPokemonWorld.screen.blit(pokemon.image,pokemon.rect)
                        KingOfBet_LostInPokemonWorld.screen.blit(door_image,door_rect)
                        clock.tick(30)
                        pg.display.flip()
                startIntro=False
                maps[mapLength][map].draw(KingOfBet_LostInPokemonWorld.screen)
            for pokemon in range(0,len(pokemons)):
                if (pokemons[pokemon].rect.left>=maps[mapLength][map].vachDich) and (pokemons[pokemon] not in finish):
                    finish.append(pokemons[pokemon])
                    rank.append(pokemon)
                if (pokemons[pokemon].rect.left>=maps[mapLength][map].vachDich+10) and (pokemons[pokemon] in finish) and (pokemons[pokemon] not in stop):
                    stop.append(pokemons[pokemon])
            if maps[mapLength][map].move:
                for i in range (0,len(buas)):
                    if buaMoves[i]:
                        buaPos[i].left-=1
            for event in pg.event.get():
                if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONUP:
                    if pg.mouse.get_pressed():
                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                        x_mouse,y_mouse=pg.mouse.get_pos()
                        if menu_rect.collidepoint(x_mouse,y_mouse):
                            watching=True
                            KingOfBet_LostInPokemonWorld.screen.blit(menuBoard_image,menuBoard_rect)
                            if Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.screen.blit(mute_image,mute_rect)
                            else:
                                KingOfBet_LostInPokemonWorld.screen.blit(unMute_image,unMute_rect)
                            KingOfBet_LostInPokemonWorld.screen.blit(quitOption_image,quitOption_rect)
                            KingOfBet_LostInPokemonWorld.screen.blit(x_image,x_rect)
                            pg.display.flip()
                            while watching:
                                for event in pg.event.get():
                                    if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                        pg.display.quit()
                                        pg.quit()
                                        sys.exit()
                                    if event.type == pg.MOUSEBUTTONUP:
                                        if pg.mouse.get_pressed():
                                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                            x_mouse,y_mouse=pg.mouse.get_pos()
                                            if mute_rect.collidepoint(x_mouse,y_mouse):
                                                if Variable.muteOrNot:
                                                    Variable.muteOrNot=False
                                                    KingOfBet_LostInPokemonWorld.screen.blit(menuBoard_image,menuBoard_rect)
                                                    if Variable.muteOrNot:
                                                        KingOfBet_LostInPokemonWorld.screen.blit(mute_image,mute_rect)
                                                    else:
                                                        KingOfBet_LostInPokemonWorld.screen.blit(unMute_image,unMute_rect)
                                                    KingOfBet_LostInPokemonWorld.screen.blit(quitOption_image,quitOption_rect)
                                                    KingOfBet_LostInPokemonWorld.screen.blit(x_image,x_rect)
                                                    pg.display.flip()
                                                    KingOfBet_LostInPokemonWorld.channel3.set_volume(1)
                                                    KingOfBet_LostInPokemonWorld.channel1.set_volume(1)
                                                    KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                                                else:
                                                    KingOfBet_LostInPokemonWorld.channel3.set_volume(0)
                                                    KingOfBet_LostInPokemonWorld.channel1.set_volume(0)
                                                    KingOfBet_LostInPokemonWorld.channel2.set_volume(0)
                                                    Variable.muteOrNot=True
                                                    KingOfBet_LostInPokemonWorld.screen.blit(menuBoard_image,menuBoard_rect)
                                                    if Variable.muteOrNot:
                                                        KingOfBet_LostInPokemonWorld.screen.blit(mute_image,mute_rect)
                                                    else:
                                                        KingOfBet_LostInPokemonWorld.screen.blit(unMute_image,unMute_rect)
                                                    KingOfBet_LostInPokemonWorld.screen.blit(quitOption_image,quitOption_rect)
                                                    KingOfBet_LostInPokemonWorld.screen.blit(x_image,x_rect)
                                                    pg.display.flip()
                                            if quitOption_rect.collidepoint(x_mouse,y_mouse):
                                                Money-=betGoldInt
                                                Variable.playerMoneys[ID-1]=Money
                                                Module.writeData(ID)
                                                KingOfBet_LostInPokemonWorld.main(ID,playerName,Money)
                                            if x_rect.collidepoint(x_mouse,y_mouse):
                                                watching=False
                if event.type == pg.KEYDOWN:
                    if event.key==pg.K_F1:
                        selectDefaultCamera=0
                        cameras[0]='Yes'
                        for i in (1,2,3,4):
                            cameras[i]="No"
                    if event.key==pg.K_F2:
                        selectDefaultCamera=0
                        cameras[1]='Yes'
                        for i in (0,2,3,4):
                            cameras[i]="No"
                    if event.key==pg.K_F3:
                        selectDefaultCamera=0
                        cameras[2]='Yes' 
                        for i in (1,0,3,4):
                            cameras[i]="No"
                    if event.key==pg.K_F4:
                        selectDefaultCamera=0
                        cameras[3]='Yes'
                        for i in (1,2,0,4):
                            cameras[i]="No"
                    if event.key==pg.K_F5:
                        selectDefaultCamera=0
                        cameras[4]='Yes'
                        for i in (1,2,3,0):
                            cameras[i]="No"
                    if event.key==pg.K_LCTRL:
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                            hieuUng=None
                            i=9
                            if i==9:
                                if data[i+2]=='sold':
                                    data[i+2]='notsold'
                                    Module.updateCuaHang(playerName,data)
                                    hieuUng=random.randint(1,7)
                                    pokemons[pokemonSelection].bua(hieuUng)
                                    if hieuUng==2:
                                        hieuUngStun=True
                                        pokemonStun=pokemonSelection
                                        countStun=0
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.stunSound)
                                        stunEffect.rect.left=pokemons[pokemonSelection].rect.left+pokemons[pokemonSelection].rect.width/3
                                        stunEffect.rect.top=pokemons[pokemonSelection].rect.top+10
                                    elif hieuUng==1:
                                        hieuUngBoot=True
                                        pokemonBoot=pokemonSelection
                                        countBoot=0
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
                                        bootEffect.rect.left=pokemons[pokemonSelection].rect.left-30
                                        bootEffect.rect.bottom=pokemons[pokemonSelection].rect.bottom+10
                                    elif hieuUng==5:
                                        hieuUngSlow=True
                                        countSlow=0
                                        slowPokemon=pokemons[pokemonSelection]
                                        pokemons[pokemonSelection].spriteSpeed=0.05
                                        slowEffect.rect.left=pokemons[pokemonSelection].rect.width/3+pokemons[pokemonSelection].rect.left
                                        slowEffect.rect.top=pokemons[pokemonSelection].rect.top
                                    elif hieuUng in (3,4,6):
                                        if hieuUng==3:
                                            pokemons[pokemonSelection].rect.left=maps[mapLength][map].bgLeft+1420
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                                    else:
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
                                else:
                                    i+=1
                            if i==10:
                                if data[i+2]=='sold':
                                    data[i+2]='notsold'
                                    Module.updateCuaHang(playerName,data)
                                    hieuUng=random.choice((1,4,6,7))
                                    pokemons[pokemonSelection].bua(hieuUng)
                                    if hieuUng==1:
                                        hieuUngBoot=True
                                        pokemonBoot=pokemonSelection
                                        countBoot=0
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
                                        bootEffect.rect.left=pokemons[pokemonSelection].rect.left-30
                                        bootEffect.rect.bottom=pokemons[pokemonSelection].rect.bottom+10
                                    elif hieuUng in (4,6):
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                                    else:
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
                                else:
                                    i+=1
                            if i==11:
                                if data[i+2]=='sold':
                                    data[i+2]='notsold'
                                    Module.updateCuaHang(playerName,data)
                                    hieuUng=random.choice((1,1,4,4,6,7))
                                    pokemons[pokemonSelection].bua(hieuUng)
                                    if hieuUng==1:
                                        hieuUngBoot=True
                                        pokemonBoot=pokemonSelection
                                        countBoot=0
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
                                        bootEffect.rect.left=pokemons[pokemon].rect.left-30
                                        bootEffect.rect.bottom=pokemons[pokemon].rect.bottom+10
                                    elif hieuUng in (4,6):
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                                    else:
                                        if not Variable.muteOrNot:
                                            KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                                        KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
            for bua in range(0,len(buas)):
                for pokemon in range(0,len(pokemons)):
                    if pokemons[pokemon].rect.colliderect(buaPos[bua]):# cái này là dính bùa
                        buaMoves[bua]=False
                        buaPos[bua].top=-1000
                        pokemons[pokemon].bua(hieuUngs[bua])
                        if hieuUngs[bua]==2:
                            hieuUngStun=True
                            countStun=0
                            pokemonStun=pokemon
                            if not Variable.muteOrNot:
                                 KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.stunSound)
                            stunEffect.rect.left=pokemons[pokemon].rect.left+pokemons[pokemon].rect.width/3
                            stunEffect.rect.top=pokemons[pokemon].rect.top+10
                        elif hieuUngs[bua]==1:
                            hieuUngBoot=True
                            countBoot=0
                            pokemonBoot=pokemon
                            if not Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.bootSound)
                            bootEffect.rect.left=pokemons[pokemon].rect.left-30
                            bootEffect.rect.bottom=pokemons[pokemon].rect.bottom+10
                        elif hieuUngs[bua]==5:
                            hieuUngSlow=True
                            countSlow=0
                            slowPokemon=pokemons[pokemon]
                            pokemons[pokemon].spriteSpeed=0.05
                            slowEffect.rect.left=pokemons[pokemon].rect.width/3+pokemons[pokemon].rect.left
                            slowEffect.rect.top=pokemons[pokemon].rect.top
                        elif hieuUngs[bua]==3:
                            pokemons[pokemon].rect.left=maps[mapLength][map].bgLeft+1420
                            if not Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                        elif hieuUngs[bua]==4:
                            hieuUngForward=True
                            countForward=0
                            forwardPokemon=pokemon
                            forwardEffect.rect.left=pokemons[pokemon].rect.width/3+pokemons[pokemon].rect.left+100
                            forwardEffect.rect.bottom=pokemons[pokemon].rect.bottom
                            if not Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                        elif hieuUngs[bua]==6:
                            hieuUngBackward=True
                            countBackward=0
                            backwardPokemon=pokemon
                            backwardEffect.rect.left=pokemons[pokemon].rect.width/3+pokemons[pokemon].rect.left-100
                            backwardEffect.rect.bottom=pokemons[pokemon].rect.bottom
                            if not Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                        elif hieuUngs[bua]==7:
                            hieuUngReverse=True
                            reversePokemon=pokemon
                            reverseEffect.rect.left=pokemons[pokemon].rect.width/3+pokemons[pokemon].rect.left
                            reverseEffect.rect.top=pokemons[pokemon].rect.top-10
                            countReverse=0
                        elif hieuUngs[bua] ==8:
                            pokemons[pokemon].rect.left=maps[mapLength][map].vachDich+30
                            rank.append(pokemon)
                            finish.append(pokemons[pokemon])
                            stop.append(pokemons[pokemon])
                            if not Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
                        else:
                            if not Variable.muteOrNot:
                                KingOfBet_LostInPokemonWorld.channel2.set_volume(0.5)
                            KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.teleportSound)
            for i in range (0,len(buas)):
                KingOfBet_LostInPokemonWorld.screen.blit(buas[i],buaPos[i])
            #cập nhật sprites:
            pokemon=random.choice(pokemons)
            if pokemon.stunOrBoot!='stun' and pokemon not in stop:
                pokemon.rect.left+= random.choice(step)
            for pokemon in pokemons:
                if pokemon.stunOrBoot=="reverse":
                    pokemon.rect.left-=2
                if pokemon==pokemons[pokemonSelection]:
                    Module.printing('JosefinSans-BoldItalic.ttf',24,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,f'{playerName}',(pokemon.rect.left+60,pokemon.rect.top+pokemon.rect.height+5))
                else:
                    Module.printing('JosefinSans-BoldItalic.ttf',24,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,f'player {num}',(pokemon.rect.left+60,pokemon.rect.top+pokemon.rect.height+10))
                if pokemon not in stop:
                    pokemon.update(maps[mapLength][map].move)
                    if pokemon.stunOrBoot not in ("stun","reverse") :
                        pokemon.rect.left+=len(finish)
                    KingOfBet_LostInPokemonWorld.screen.blit(pokemon.image,pokemon.rect)
                else:
                    pokemon.current_sprite=0
                    pokemon.rect.left=maps[mapLength][map].vachDich
                    KingOfBet_LostInPokemonWorld.screen.blit(pokemon.image,pokemon.rect)
                num+=1
            if hieuUngStun:
                stunEffect.update(maps[mapLength][map].move)
                KingOfBet_LostInPokemonWorld.screen.blit(stunEffect.image,(stunEffect.rect.left,stunEffect.rect.top))
                stunEffect.rect.left=pokemons[pokemonStun].rect.left+pokemons[pokemonStun].rect.width/3
                stunEffect.rect.top=pokemons[pokemonStun].rect.top+10
                countStun+=1
                if countStun>100:
                    pokemonStun=None
                    if not Variable.muteOrNot:
                        KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                    hieuUngStun=False
            if hieuUngSlow:
                slowEffect.update(maps[mapLength][map].move)
                KingOfBet_LostInPokemonWorld.screen.blit(slowEffect.image,(slowEffect.rect.left,slowEffect.rect.top))
                if maps[mapLength][map].move:
                    slowEffect.rect.left=slowPokemon.rect.left+slowPokemon.rect.width/3
                countSlow+=1
                if countSlow>150:
                    slowPokemon=None
                    hieuUngSlow=False
            if hieuUngBoot:
                bootEffect.update(maps[mapLength][map].move)
                KingOfBet_LostInPokemonWorld.screen.blit(bootEffect.image,(bootEffect.rect.left,bootEffect.rect.top))
                bootEffect.rect.left=pokemons[pokemonBoot].rect.left-30
                bootEffect.rect.bottom=pokemons[pokemonBoot].rect.bottom+10
                countBoot+=2
                if countBoot>125:
                    if not Variable.muteOrNot:
                        KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                    pokemonBoot=None
                    hieuUngBoot=False
            if hieuUngBackward:
                backwardEffect.update(maps[mapLength][map].move)
                backwardEffect.rect.left-=1
                KingOfBet_LostInPokemonWorld.screen.blit(backwardEffect.image,backwardEffect.rect)
                countBackward+=1
                if countBackward>50:
                    hieuUngBackward=False
                    backwardPokemon=None
            if hieuUngForward:
                forwardEffect.update(maps[mapLength][map].move)
                forwardEffect.rect.left-=1
                KingOfBet_LostInPokemonWorld.screen.blit(forwardEffect.image,forwardEffect.rect)
                countForward+=1
                if countForward>50:
                    hieuUngForward=False
                    forwardPokemon=None
            if hieuUngReverse:
                reverseEffect.update(maps[mapLength][map].move)
                reverseEffect.rect.left=pokemons[reversePokemon].rect.width/3+pokemons[reversePokemon].rect.left
                reverseEffect.rect.top=pokemons[reversePokemon].rect.top-10
                KingOfBet_LostInPokemonWorld.screen.blit(reverseEffect.image,reverseEffect.rect)
                countReverse+=1
                if countReverse==150:
                    hieuUngReverse=False
            if maps[mapLength][map].move:
                for pokemon in pokemons:
                    if pokemon not in stop and (pokemon.stunOrBoot!='stun') and (pokemon.stunOrBoot!='slow'):
                        pokemon.rect.left+=1
            for i in range (0,len( cameras)):
                if cameras[i]=="Yes":
                    distance=1366/2-pokemons[i].rect.left-round(pokemons[i].rect.width/2)
                    forwardEffect.rect.left+=distance
                    backwardEffect.rect.left+=distance
                    for pokemon in pokemons:
                        pokemon.rect.left+=distance
                    for bua in buaPos:
                        bua.left+=distance
                    maps[mapLength][map].bgLeft+=distance
                    maps[mapLength][map].quangDuong-=distance
                    maps[mapLength][map].vachDich+=distance
                    for i in range(0,len(playerCoVu)):
                        playerCoVu[i].rect.left+=distance
                    fountain.rect.left+=distance
            clock.tick(60)
            pg.display.flip() # cập nhật màn hình 
            if len(finish)==5:# cái này ăn mừng
                if pokemons[pokemonSelection]==finish[0]:
                    KingOfBet_LostInPokemonWorld.screen.blit(win1_image,win1_rect)
                    pg.display.flip()
                    pg.time.delay(2000)
                else:
                    KingOfBet_LostInPokemonWorld.screen.blit(lose_image,lose_rect)
                    pg.display.flip()
                    pg.time.delay(2000)
                if predictionList==finish:
                    Money+=10
                    Variable.playerMoneys[ID-1]=Money
                    Module.writeData(ID)
                anmungTime=True
                pokemon_pos=[(700,310),(180,445),(390,445),(1000,445),(1210,445)]
                light.rect.center=(700,260)
                for pokemon in range(0,len(finish)):
                    finish[pokemon].rect.center=pokemon_pos[pokemon]
                    anmung[pokemon].spriteSpeed=0.15
                countUp=0
                if not Variable.muteOrNot:
                    KingOfBet_LostInPokemonWorld.channel2.set_volume(0)
                KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.anmungSound)
                while anmungTime:
                    for event in pg.event.get():
                        if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                            pg.display.quit()
                            pg.quit()
                            sys.exit()
                    KingOfBet_LostInPokemonWorld.screen.blit(podium_image,(0,0))
                    for pokemon in range(0,len(finish)):
                        if pokemon==0:
                            anmung[rank[0]].update(maps[mapLength][map].move)
                            KingOfBet_LostInPokemonWorld.screen.blit(anmung[rank[0]].image,finish[0].rect)
                        else:
                            anmung[rank[pokemon]].update(maps[mapLength][map].move)
                            KingOfBet_LostInPokemonWorld.screen.blit(anmung[rank[pokemon]].image,finish[pokemon].rect)
                    flower.update(maps[mapLength][map].move)
                    KingOfBet_LostInPokemonWorld.screen.blit(flower.image,flower.rect)
                    light.update(maps[mapLength][map].move)
                    KingOfBet_LostInPokemonWorld.screen.blit(light.image,light.rect)
                    clock.tick(60)
                    pg.display.flip()
                    countUp+=1
                    if countUp>=400:
                        anmungTime=False
                        result=0
                    if not KingOfBet_LostInPokemonWorld.channel3.get_busy():
                        if not Variable.muteOrNot:
                            KingOfBet_LostInPokemonWorld.channel2.set_volume(1)
                    clock.tick(60)
                    pg.display.flip() # cập nhật màn hình 
            if result==0:# cái này hiện kết quả
                betMoney.append(int(betGold))
                betName.append(pokemons[pokemonSelection].name)
                if pokemons[pokemonSelection]==finish[0]:
                    betResult.append('WIN')
                    Money+=betGoldInt
                    total+=betGoldInt
                    Variable.playerMoneys[ID-1]=Money
                    Module.writeData(ID)
                else:
                    betResult.append('LOSE')
                    Money-=betGoldInt
                    total-=betGoldInt
                    Variable.playerMoneys[ID-1]=Money
                    Module.writeData(ID)
                if predictionList==finish:
                    predictionResult.append('Right')
                else:
                    predictionResult.append('Wrong')
                predictionPos=[(345,85),(345,230),(345,380),(345,525),(345,675)]
                resultPos=[(1160,85),(1160,230),(1160,380),(1160,525),(1160,675)]
                resultTime=True
                quit_rect.center=(670,700)
                retry_rect.center=(670,600)
                history_rect.center=(650,500)
                while resultTime:
                    for event in pg.event.get():
                        if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                            pg.display.quit()
                            pg.quit()
                            sys.exit()
                        if event.type == pg.MOUSEBUTTONUP:
                            if pg.mouse.get_pressed():
                                KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                x_mouse,y_mouse=pg.mouse.get_pos()
                            if retry_rect.collidepoint(x_mouse,y_mouse):# cái này chơi lại
                                resultTime=False
                                result=1
                                play=1
                                chooseLength=0
                            if quit_rect.collidepoint(x_mouse,y_mouse):# cái này out game
                                stopPlaying=True
                                KingOfBet_LostInPokemonWorld.screen.fill((250 ,229, 89))
                                KingOfBet_LostInPokemonWorld.screen.blit(moneyNotification_image,(200,50))
                                Module.printing('JosefinSans-BoldItalic.ttf',40,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,f' {Money}',(500,404))
                                quit_rect.center=(350,500)
                                KingOfBet_LostInPokemonWorld.screen.blit(quit_image,quit_rect)
                                KingOfBet_LostInPokemonWorld.screen.blit(history_image,history_rect)
                                pg.display.flip()
                                while stopPlaying:
                                    for event in pg.event.get():
                                        if event.type == pg.QUIT: # thoát nếu chọn nút X hoặc alt f4
                                            pg.display.quit()
                                            pg.quit()
                                            sys.exit()
                                        if event.type == pg.MOUSEBUTTONUP:
                                            if pg.mouse.get_pressed():
                                                KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                x_mouse,y_mouse=pg.mouse.get_pos()
                                            if history_rect.collidepoint(x_mouse,y_mouse):    # chỗ này hiện bảng bet history
                                                KingOfBet_LostInPokemonWorld.screen.blit(bettingHistory_image,(800,65))
                                                KingOfBet_LostInPokemonWorld.screen.blit(quit_image,quit_rect)
                                                Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,'Pokemon   Bet    Result   Prediction',(1050,180))
                                                for i in range(0,len(betMoney)):
                                                    Module.printing('JosefinSans-BoldItalic.ttf',20,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,f'{resultData[0][i]}       {resultData[1][i]}      {resultData[2][i]}      {resultData[3][i]}',(1050,220+i*45))
                                                    data.append(f'{resultData[0][i]}-{resultData[1][i]}-{resultData[2][i]}-{resultData[3][i]}')
                                                Module.updateCuaHang(playerName,data)
                                                Module.printing('JosefinSans-BoldItalic.ttf',30,KingOfBet_LostInPokemonWorld.screen,Variable.nenSangFont,f'{total}',(1200,650))
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
                                                                KingOfBet_LostInPokemonWorld.channel3.play(KingOfBet_LostInPokemonWorld.nhannut)
                                                                x_mouse,y_mouse=pg.mouse.get_pos()
                                                            if quit_rect.collidepoint(x_mouse,y_mouse): # cái này out game
                                                                KingOfBet_LostInPokemonWorld.channel2.fadeout(1000)
                                                                KingOfBet_LostInPokemonWorld.main(ID,playerName,Money)
                                            if quit_rect.collidepoint(x_mouse,y_mouse): # cái này cx out game
                                                KingOfBet_LostInPokemonWorld.channel2.fadeout(1000)
                                                KingOfBet_LostInPokemonWorld.main(ID,playerName,Money)
                    KingOfBet_LostInPokemonWorld.screen.blit(endResult_image,(0,0))
                    if betResult[len(betResult)-1]=="WIN":
                        Module.printing('JosefinSans-BoldItalic.ttf',36,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,f'+ {betGoldInt} gold',(670,200))
                    else:
                        Module.printing('JosefinSans-BoldItalic.ttf',36,KingOfBet_LostInPokemonWorld.screen,Variable.nenToiFont,f'- {betGoldInt} gold',(670,200))
                    KingOfBet_LostInPokemonWorld.screen.blit(retry_image,retry_rect)
                    KingOfBet_LostInPokemonWorld.screen.blit(quit_image,quit_rect)
                    pokemonList[map].update(maps[mapLength][map].move)
                    for i in range (0,len(pokemons)):
                        predictionList[i].rect.center=predictionPos[i]
                        KingOfBet_LostInPokemonWorld.screen.blit(predictionList[i].image,predictionList[i].rect)
                        finish[i].rect.center=resultPos[i]
                        KingOfBet_LostInPokemonWorld.screen.blit(finish[i].image,finish[i].rect)
                    clock.tick(60)
                    pg.display.flip()
            if not KingOfBet_LostInPokemonWorld.channel3.get_busy():
                if not Variable.muteOrNot:
                    KingOfBet_LostInPokemonWorld.channel2.set_volume(1)