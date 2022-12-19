import pygame as pg

pg.init()

sc = pg.display.set_mode((1200,800))


icon = pg.image.load("spaceship.png")

pg.display.set_caption("Space Invader")
pg.display.set_icon(icon)



p1 = pg.image.load("main.png")
PX = 600
PY = 700
def player(a,b):
    sc.blit(p1,(a,b))



op = True
while op:
    sc.fill((0,0,0))
    for events in pg.event.get():
        px = 0
        if events.type == pg.QUIT:
            op = False

        if events.type == pg.KEYDOWN:
            if events.key == pg.K_LEFT:
                px = -1
            if events.key == pg.K_RIGHT:
                px = 1
        if events.type == pg.KEYUP:
            if events.key == pg.K_LEFT or events.key == pg.K_RIGHT:
                px = 0
    if PX <= 0  :
        PX = 0
    if PX >= 1170 :
        PX = 1170
        
    #print(PX)
    PX += px
    player(PX,PY)
    pg.display.update()
