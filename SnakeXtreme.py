import pygame
import random
from time import sleep
pygame.init()
screen=pygame.display.set_mode((800,500))
run=True
pygame.display.set_caption('Snake Game By Srinivas Makkena')
x=random.randint(2,77)*10
y=random.randint(2,44)*10
fy=random.randint(3,43)
fx=random.randint(3,75)
dx=dy=0
def player():
    screen.blit(im,(x,y))
def pixel(surface, color, pos):
    surface.fill(color, (pos, (10, 10)))
def food(surface,color,pos):
    surface.fill(color,(pos, (10, 10)))
lq=1
font = pygame.font.Font('freesansbold.ttf', 20)
q=[]
for i in range(5):
    screen.fill((0,150,0))
    text = font.render('Welcome to my snake game', True,(0,0,0))
    screen.blit(text, [290,210])
    text1 = font.render('game will start in : '+str(5-(i+1))+'sec', True,(255,0,0))
    screen.blit(text1, [300,230])
    pygame.display.update()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
            pygame.quit()
    sleep(1)
ls=0
ss=0.2
si=1
s=1
while run:
    ls+=1
    if(ls>150):
        ls=0
        ss-=0.01
        si+=1
    if(ss<=0.05 and lq>=150):
        run=False
        screen.fill((0,150,0))
        text1 = font.render("You Won The Game.¯\_('_')_/¯", True,(0,0,255))
        text2 = font.render('Your Final Score is '+str(lq-1), True,(0,0,255))
        text3 = font.render(' Thank you for playing.', True,(0,0,255))
        text4 = font.render(" ^_^ ", True,(0,0,255))
        screen.blit(text1, [290,180])
        screen.blit(text2, [270,210])
        screen.blit(text3, [280,240])
        screen.blit(text4, [370,280])
        pygame.display.update()
        sleep(3)
        pygame.quit()
    elif(lq<150 and ss<=0.05):
        run=False
        screen.fill((0,150,0))
        text1 = font.render('You Loss The Game.(•_•)', True,(0,0,255))
        text2 = font.render('Your Final Score is '+str(lq-1), True,(0,0,255))
        text3 = font.render(' Thank you for playing.', True,(0,0,255))
        text4 = font.render(" ^_^ ", True,(0,0,255))
        screen.blit(text1, [290,180])
        screen.blit(text2, [270,210])
        screen.blit(text3, [280,240])
        screen.blit(text4, [370,280])
        pygame.display.update()
        sleep(3)
        pygame.quit()
    screen.fill((0,150,0))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 500), 20)
    pygame.draw.rect(screen, (255,255,255), (0, 0, 800, 500), 5)
    text = font.render('Your Score is '+str(lq-1), True,(0,0,255))
    screen.blit(text, [350,460])
    x+=dx
    y+=dy
    if((x<=0 and dx<0)):
        x=780
    if(x>=790 and dx>0):
        x=10
    if((y<=0 and dy<0)):
        y=450
    if((y>=460 and dy>0)):
        y=10
    pygame.display.update()
    q.append((x,y))
    q=q[-s:]
    food(screen,(200,0,0),(fx*10,fy*10))
    c=0
    for i in q:
        pixel(screen,(255,255,255),i)
        if(q[0][0]==i[0] and q[0][1]==i[1] and c!=0):
            run=False
            screen.fill((0,150,0))
            text = font.render('Your Final Score is '+str(lq-1), True,(0,0,255))
            text2 = font.render(' Thank you for playing.', True,(0,0,255))
            text4 = font.render(" ^_^ ", True,(0,0,255))
            screen.blit(text, [290,210])
            screen.blit(text2, [280,240])
            screen.blit(text4, [370,280])
            pygame.display.update()
            sleep(3)
            pygame.quit()
        c+=1
    if(q[-1]==(fx*10,fy*10)):
        fy=random.randint(3,43)
        fx=random.randint(3,75)
        lq+=si
        s+=1
    pygame.display.update()
    sleep(ss)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
            screen.fill((0,150,0))
            text = font.render('Your Final Score is '+str(lq-1), True,(0,0,255))
            text2 = font.render(' Thank you for playing.', True,(0,0,255))
            text4 = font.render(" ^_^ ", True,(0,0,255))
            screen.blit(text, [290,210])
            screen.blit(text2, [280,240])
            screen.blit(text4, [370,280])
            pygame.display.update()
            sleep(3)
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                if(dx==0):
                    dx-=10
                    dy=0
            if i.key==pygame.K_RIGHT:
                if(dx==0):
                    dx+=10
                    dy=0
            if i.key==pygame.K_UP:
                if(dy==0):
                    dy-=10
                    dx=0
            if i.key==pygame.K_DOWN:
                if(dy==0):
                    dy+=10
                    dx=0
