import pygame as pg
from random import *
from time import *


"screen setup"
pg.init()
sc = pg.display.set_mode((1200,800))

"icon image loaded"
icon = pg.image.load("spaceship.png")


"setup for title and icon"
pg.display.set_caption("Space invader")
pg.display.set_icon(icon)


"player image load and setup at perticular co-ordinates"
p1 = pg.image.load("main.png")
PX = 600
PY = 700
def player(a,b):
    sc.blit(p1,(a,b))


"alien image loaded and setup at random coordinates"
alien1 = pg.image.load("alien.png")
AX = randint(0,1136)
AY = randint(10,260)
ax = 0.5
ay = 0.5

"for bullets"
bullets = pg.image.load("bullet.png")
BX = 0
BY = 700
bx = 0
by = 40
b_state = "ready"

"functions to define objects differently"
def alien(a,b):
    sc.blit(alien1,(a,b))

def shoot(a,b):
    global b_state
    b_state = "fire"
    sc.blit(bullets,(a+4,b+9))
    global BY
    BY -= 4

    


def collide(a,b):
    if AX == PX and AY == PY :
        pass

"background loaded and setup for full screen"
background = pg.image.load("back.jpg")

"main loop"
op = True
while op:
    "bloack canvas is made"
    sc.fill((0,0,0))
    "background is displayed or drawn "
    sc.blit(background,(0,0))

    "for quitiing or getting events for keypresses"
    for events in pg.event.get():
        px = 0
        
        if events.type == pg.QUIT:
            op = False
        "for bullets and shooting"
        
        "for spaceship movement"
        if events.type == pg.KEYDOWN:
            if events.key == pg.K_LEFT:
                px = -1
            if events.key == pg.K_RIGHT:
                px = 1
            if events.key == pg.K_UP:
                px = -1
            if events.key == pg.K_DOWN:
                px = 1
            if events.key == pg.K_SPACE:
                if b_state == "ready":
                    BX = PX
                    shoot(BX,BY)
        if events.type == pg.KEYUP:
            if events.key == pg.K_LEFT or events.key == pg.K_RIGHT:
                px = 0
           

    "for spaceship"
    if PX <= 0  :
        PX = 0
    if PX >= 1170 :
        PX = 1170
    
    
    PX += px
    "for alien movement mechanics"
    if  AX <= 0 :
        AY += 25
        ax = 0.5
            
    if AX == 1136 :
        AY += 25  
        ax = -0.5
    AX += ax


    if BY <= 0 :
        BY = 700
        b_state = "ready"


    if b_state == "fire":
        shoot(BX,BY)
    
        
    
                
    "player and alien setup and drawn last to show on top of all layers"
    player(PX,PY)
    alien(AX,AY)
    pg.display.update()
