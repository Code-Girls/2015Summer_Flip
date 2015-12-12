# 1 - Import library
import pygame
from pygame.locals import *
import math
import random 

# 2 - Initialize the game
pygame.init()
width, height = 750, 500
screen = pygame.display.set_mode((width, height))
keys = [False]
tap = 0
taprequire = []
pygame.mixer.init()
human = 0
running = 1
count2 = 0
count3 = 0
count4 = 0
stage = 0
stageTwoStart = pygame.time.get_ticks()

# 3 - Load image
#3.1 - load background images
bgopen = pygame.image.load("images/background/open_scene.png")
bg0 = pygame.image.load("images/background/background_0.png")
bg1 = pygame.image.load("images/background/background_1.png")
bg2 = pygame.image.load("images/background/background_2.png")
bg3 = pygame.image.load("images/background/background_3.png")
bg4 = pygame.image.load("images/background/background_4.png")
bgover = pygame.image.load("images/background/background_gameover.png")
#3.2 - load cover images
angel = pygame.image.load("images/cover/angel.png")
angeldes = pygame.image.load("images/cover/angeldes.png")
jessica = pygame.image.load("images/cover/jessica.png")
jessicades = pygame.image.load("images/cover/jessicades.png")
title = pygame.image.load("images/cover/title.png")
instruction = pygame.image.load("images/cover/instruction.png")
gif = pygame.image.load("images/book/gif.gif")
#3.3 - load elements images
bluebar = pygame.image.load("images/elements/bluebar.jpg")
redbar1 = pygame.image.load("images/elements/redbar1.jpg")
redbar2 = pygame.image.load("images/elements/redbar2.jpg")
redbar3 = pygame.image.load("images/elements/redbar3.jpg")
redbar4 = pygame.image.load("images/elements/redbar4.jpg")
contin = pygame.image.load("images/elements/contin.png")
pages = pygame.image.load("images/elements/pages.png")
quit1 = pygame.image.load("images/elements/quit.png")
ready = pygame.image.load("images/elements/ready.png")
taprequire1 = pygame.image.load("images/elements/taprequire1.png")
taprequire2 = pygame.image.load("images/elements/taprequire2.png")
taprequire3 = pygame.image.load("images/elements/taprequire3.png")
taprequire4 = pygame.image.load("images/elements/taprequire4.png")
sett = pygame.image.load("images/elements/sett.png")
start = pygame.image.load("images/elements/start.png")
level1 = pygame.image.load("images/elements/level1.png")
level2 = pygame.image.load("images/elements/level2.png")
level3 = pygame.image.load("images/elements/level3.png")
level4 = pygame.image.load("images/elements/level4.png")
#3.4 - load win or lose images
win1 = pygame.image.load("images/losewin/win1.png")
win2 = pygame.image.load("images/losewin/win2.jpg")
win3 = pygame.image.load("images/losewin/win3.png")
win4 = pygame.image.load("images/losewin/win4.png")
win5 = pygame.image.load("images/losewin/win5.png")
lose1 = pygame.image.load("images/losewin/lose1.png")
lose2 = pygame.image.load("images/losewin/lose2.png")
#3.5 - load certificate
win00 = pygame.image.load("images/certificate/win00.png")
win11 = pygame.image.load("images/certificate/win11.png")
win22 = pygame.image.load("images/certificate/win22.png")
win33 = pygame.image.load("images/certificate/win33.png")
win44 = pygame.image.load("images/certificate/win44.png")
win55 = pygame.image.load("images/certificate/win55.png")
#3.6 - load books
book0 = pygame.image.load("images/book/book0.png")
book1 = pygame.image.load("images/book/book1.png")
book2 = pygame.image.load("images/book/book2.png")
book3 = pygame.image.load("images/book/book3.png")

# 4 Load Audio
clap = pygame.mixer.Sound("audio/clap.mp3")
click = pygame.mixer.Sound("audio/click.wav")
click1 = pygame.mixer.Sound("audio/click.wav")
fail = pygame.mixer.Sound("audio/fail.wav")
turn = pygame.mixer.Sound("audio/flip.mp3")
levelup = pygame.mixer.Sound("audio/levelup.wav")
clap.set_volume(3.0)
click.set_volume(0.19)
click1.set_volume(0.5)
fail.set_volume(0.2)
turn.set_volume(3.0)
levelup.set_volume(0.05)
pygame.mixer.music.load("audio/background.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(1.0)

levelOneStartTime = 1000000000
levelOneStart = 0 
levelTwoStartTime = 1000000000
levelTwoStart = 0 
levelThreeStartTime = 1000000000
levelThreeStart = 0
levelFourStartTime = 1000000000
levelFourStart = 0

# 5 - set up settings
#5.0 - openning scene
screen.blit(bgopen,(0,0))
pygame.display.flip()
pygame.time.wait(3000)
#5.1 - choosing character
time = 0
screen.blit(bg0,(0,0))
screen.blit(instruction,(230,55))
screen.blit(angel,(230,120))
screen.blit(angeldes,(250, 300))
screen.blit(jessica,(430,120))
screen.blit(jessicades,(435, 300))
trecord = 0

 # update the screen
pygame.display.flip()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
count = 0
while running:
    screen.fill(0)
    screen.blit(bg0,(0,0))
    screen.blit(instruction,(230,55))
    screen.blit(angel,(230,120))
    screen.blit(angeldes,(250, 300))
    screen.blit(jessica,(430,120))
    screen.blit(jessicades,(435, 300))
    
    # character selection
    if stage == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] > 375:
                    human = 0
                    stage = 1
                else:
                    human = 1
                    stage = 1

   
    # entering level 1
    if stage == 1:
        taprequire = 80
        time = 1
        screen.blit(bg1,(0,0))
        screen.blit(level1,(580,50))
        screen.blit(quit1,(610,430))
        screen.blit(redbar1,(100,50))
        
        if human == 0:                      #character jessica shows up
            screen.blit(jessica,(330,300))
            screen.blit(book0,(350,390))
      
        if human == 1:                      #character angel shows up
            screen.blit(angel,(330,300))
            screen.blit(book0,(350,390))
            
        count += 1
        if count < 30:
            screen.blit(ready,(-100,0))
            screen.blit(taprequire1,(150,80))
            click.play()
        if 30 < count < 60:
            screen.blit(sett,(-50,0))
            screen.blit(taprequire1,(150,80))
            click.play()
        if 60 < count < 80:
            screen.blit(start,(-100,0))
            screen.blit(taprequire1,(150,80))
            click.play()
            
        # clock show up
        if count > 80:
            if levelOneStart == 0:
                levelOneStart = 1                                   # now player can start flipping books
                levelOneStartTime = pygame.time.get_ticks()         # record the tick at this moment for future calculation
            pygame.font.init()
            font = pygame.font.Font(None, 36)
            survivedtext = font.render("0:"+str((levelOneStartTime+20000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
            trecord = str((levelOneStartTime+20000-pygame.time.get_ticks())/1000%60).zfill(2)
            textRect = survivedtext.get_rect()
            textRect.topright=[600,50]
            screen.blit(survivedtext, textRect)
              

            
            #win/lose check and display
            if str((27000-pygame.time.get_ticks())/1000%60).zfill(2) == '00':
                stage = 5
            
            if tap >= taprequire:
                levelup.play()
                stage = 2
                tap = 0

                
    # entering level 2
    if stage == 2:

        taprequire = 100
        time = 1
        screen.blit(bg2,(0,0))
        screen.blit(quit1,(610,430))
        screen.blit(redbar2,(100,50))
        screen.blit(level2,(580,0))
        
        if human == 0:                      #character jessica show up
            screen.blit(jessica,(330,300))
            screen.blit(book0,(350,390))
      
        if human == 1:                      #character angel show up
            screen.blit(angel,(330,300))
            screen.blit(book0,(350,390))
    
        count2 += 1
        if count2 < 30:
            screen.blit(ready,(-100,0))
            screen.blit(taprequire2,(200,100))
            click.play()
        if 30 < count2 < 60:
            screen.blit(sett,(-50,0))
            screen.blit(taprequire2,(200,100))
            click.play()
        if 60 < count2 < 80:
            screen.blit(start,(-100,0))
            screen.blit(taprequire2,(200,100))
            click.play()
     
       
        # clock show up
        if count2 > 80:
            if levelTwoStart == 0:
                levelTwoStart = 1                                   # now player can start flipping books
                levelTwoStartTime = pygame.time.get_ticks()         # record the tick at this moment for future calculation
            pygame.font.init()
            font = pygame.font.Font(None, 36)
            survivedtext = font.render("0:"+str((levelTwoStartTime+20000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
            trecord = str((levelTwoStartTime+20000-pygame.time.get_ticks())/1000%60).zfill(2)
            textRect = survivedtext.get_rect()
            textRect.topright=[600,50]
            screen.blit(survivedtext, textRect)

   
        #use current tick minus levelTwoStart to know how long has been past since player started playing level 2
            if pygame.time.get_ticks() - levelTwoStartTime >= 20000:
                stage = 5
            if tap >= taprequire:
                stage = 3
                tap = 0

                
    # entering level 3
    if stage == 3:


        taprequire = 120
        time = 1
        screen.blit(bg3,(0,0))
        screen.blit(quit1,(610,430))
        screen.blit(redbar3,(100,50))
        screen.blit(level3,(580,0))
        
        if human == 0:                      #character jessica show up
            screen.blit(jessica,(330,300))
            screen.blit(book0,(350,390))

        if human == 1:                      #character angel show up
            screen.blit(angel,(330,300))
            screen.blit(book0,(350,390))

        count3 += 1
        if count3 < 30:
            screen.blit(ready,(-100,0))
            screen.blit(taprequire3,(150,80))
            click.play()
        if 30 < count3 < 60:
            screen.blit(sett,(-50,0))
            screen.blit(taprequire3,(150,80))
            click.play()
        if 60 < count3 < 80:
            screen.blit(start,(-100,0))
            screen.blit(taprequire3,(150,80))
            click.play()
     
       
        # clock show up
        if count3 > 80:
            if levelThreeStart == 0:
                levelThreeStart = 1                                   # now player can start flipping books
                levelThreeStartTime = pygame.time.get_ticks()         # record the tick at this moment for future calculation
            pygame.font.init()
            font = pygame.font.Font(None, 36)
            survivedtext = font.render("0:"+str((levelThreeStartTime+265000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
            trecord = str((levelThreeStartTime+25000-pygame.time.get_ticks())/1000%60).zfill(2)
            textRect = survivedtext.get_rect()
            textRect.topright=[600,50]
            screen.blit(survivedtext, textRect)

   
        #use current tick minus levelThreeStart to know how long has been past since player started playing level 3
            if pygame.time.get_ticks() - levelThreeStartTime >= 20000:
                stage = 5
            if tap >= taprequire:
                stage = 4
                tap = 0           
                
                
    # entering level 4
    if stage == 4:


        taprequire = 140
        time = 1
        screen.blit(bg4,(0,0))
        screen.blit(quit1,(610,430))
        screen.blit(redbar4,(100,50))
        screen.blit(level4,(580,0))
        
        if human == 0:                      #character jessica show up
            screen.blit(jessica,(330,300))
            screen.blit(book0,(350,390))
            
        if human == 1:                      #character angel show up
            screen.blit(angel,(330,300))
            screen.blit(book0,(350,390))
    
        count4 += 1
        if count4 < 30:
            screen.blit(ready,(-100,0))
            screen.blit(taprequire4,(150,80))
            click.play()
        if 30 < count4 < 60:
            screen.blit(sett,(-50,0))
            screen.blit(taprequire4,(150,80))
            click.play()
        if 60 < count4 < 80:
            screen.blit(start,(-100,0))
            screen.blit(taprequire4,(150,80))
            click.play()
     
       
        # clock show up
        if count4 > 80:
            if levelFourStart == 0:
                levelFourStart = 1                                   # now player can start flipping books
                levelFourStartTime = pygame.time.get_ticks()         # record the tick at this moment for future calculation
            pygame.font.init()
            font = pygame.font.Font(None, 36)
            survivedtext = font.render("0:"+str((levelFourStartTime+265000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
            trecord = str((levelFourStartTime+25000-pygame.time.get_ticks())/1000%60).zfill(2)
            textRect = survivedtext.get_rect()
            textRect.topright=[600,50]
            screen.blit(survivedtext, textRect)

   
        #use current tick minus levelFourStart to know how long has been past since player started playing level 4
            if pygame.time.get_ticks() - levelFourStartTime >= 20000:
                stage = 5
            if tap >= taprequire:
                stage = 6
                tap = 0
            
#5.3 - stage 5 - Game Over Scene
    if stage == 5:
        fail.play()
        screen.blit(bgover,(0,0))
        screen.blit(lose2,(100,180))
        screen.blit(quit1,(610,430))
        
#5.4 - stage 6 - Finish the game
    if stage == 6:
        clap.play()
        screen.blit(bg0,(0,0))
        screen.blit(win44,(120,150))
        screen.blit(quit1,(610,430))
        
    # works for all levels
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if count > 80 and event.key == pygame.K_SPACE:
                if event.key == pygame.K_SPACE:
                    click1.play()
                    screen.blit(book0,(350,390))
                    screen.blit(book1,(350,390))
                    screen.blit(book2,(350,390))
                    screen.blit(book3,(350,390))
                    tap += 1
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if 610 < position[0] < 709 and 430 < position[1] < 490:
                pygame.quit()
                exit(0)
                    

    #blue bar
    for i in range(tap):
        a = 1
        screen.blit(bluebar,(100+i*bluebar.get_width(),50))
                


    pygame.display.flip()
