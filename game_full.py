#Flappy Delcio
#MANOELA LERIPIO - ALL RIGHTS RESERVED (2021)

import pygame, random, time, sys, os
from pygame import mixer
print("Flappy Delcio")
pygame.init()
clock = pygame.time.Clock()

#########CARREGANDO OS ARQUIVOS NO TERMINAL############
try:
    pygame.display.set_icon(pygame.image.load("icon.png"))
    bird = pygame.image.load("delcio.png")
    bird2 = pygame.image.load("delcio.png")
    bird_dead = pygame.image.load("delciodie.png")
except:
    print("Está faltando algum arquivo!")
    print("Saindo...")
    pygame.quit()
    sys.exit()
window = pygame.display.set_mode((720,720))
#######CONFIGURAÇÁO DO TEXTO###############
pygame.font.init()
pygame.display.set_caption('Flappy Delcio')
font, font2 = pygame.font.SysFont('Comic Sans MS', 72), pygame.font.SysFont('Comic Sans MS', 36)
title = font.render('Flappy Delcio v1.0', True, (0,0,0), None)
caption = font2.render('Pressione ESPAÇO para começar!', True, (0,0,0), None)

########CONFIGURAÇÃO DO JOGO#######################
global start, vel, ypos, hscore, p1, p2, tscore, died
start = False
vel = 0
ypos = 300
hscore = 0
pipe = [720,random.randint(0,380)]
tscore = 0
died = False
score_sound = pygame.mixer.Sound('sounds/score_point.mp3')
endgame_sound = pygame.mixer.Sound('sounds/endgame.mp3')
transparent = (0, 0, 0, 0)
med_opacity = (0, 0, 0, 0.7)
mixer.music.load('sounds/bg.ogg')
pygame.mixer.music.play(-1)
##########INICIANDO A APLICAÇÃO####################
while True:
    window.fill((120,120,255))
    window.blit(bird2, (100, 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start == False:
                    ypos = 300
                    start = True
                vel = 7.
    if start:

        #DESAFIO DA MANUELISSIMA#
        score_sound.play()
        #DESAFIO DA MANUELISSIMA#
        window.blit(bird,(50,ypos))
        bird2.fill(transparent)
        ypos = ypos - vel
        vel = vel - 0.5
        pygame.draw.rect(window,(110,55,20),(pipe[0],0,50,pipe[1])) #COOOOREEEEESS MUDAR O 255,255 255 (RGB)#
        pygame.draw.rect(window,(200,55,20),(pipe[0],pipe[1]+300,50,720))
        window.blit(font2.render('Pontuação: ' + str(tscore), True, (0,0,0), None),(10,10))
        pipe[0] = pipe[0] - 5
        if pipe[0] < -50:
            pipe[0] = 720
            pipe[1] = random.randint(0,380)
            tscore = tscore + 1
            if tscore > hscore:
                hscore = tscore
    else:
        if died:
            #DESAFIO DA MANUELISSIMA#
            endgame_sound.play()
            #DESAFIO DA MANUELISSIMA#
            pygame.mixer.music.stop()
            window.blit(bird_dead,(100,500))
            pygame.mixer.music.play()
        window.blit(title,(100,100))
        window.blit(caption,(100,300))
        window.blit(font2.render('Maior Pontuação - ' + str(hscore), True, (0,0,0), None),(100,400))
    if (pipe[0] < 164 and pipe[0] > 14) and (ypos+192 > pipe[1]+300 or ypos < pipe[1]):
        ypos = 528
    if ypos >= 528:
        ypos = 528
        caption = font2.render('Você perdeu, poxa que pena!', True, (0,0,0), None)
        start = False
        tscore = 0
        pipe[0] = 720
        died = True
    elif ypos < 0:
        ypos = 0
        vel = -abs(vel)
    clock.tick(60)
    
#########INFO FPS CONSOLE#####
    if time.time() - int(time.time()) < 0.02 and int(time.time()) % 5 == 0:
        print("FPS: " + str(int(clock.get_fps())))
    pygame.display.flip()
    