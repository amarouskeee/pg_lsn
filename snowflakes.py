import pygame as  pg
import sys
import random  as r
from pygame.draw import circle


def setup() -> object:
    pg.init()
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    clock  = pg.time.Clock()
    return screen,clock




def main(surface: object, updater: object) -> None:
    done  =  False
    snowflakes = []
    for i in range(450):
        x =  r.randint(0,  surface.get_width())
        y = r.randint(0, surface.get_height())
        snowflakes.append((x,y))
    while not  done:
        surface.fill(pg.Color('cadetblue1'))
        for event in pg.event.get():
            if (event.type==pg.QUIT) or (event.type  ==  pg.KEYDOWN and  event.key==pg.K_ESCAPE):
                done = True
                sys.exit()
        for i in range(len(snowflakes)):
            sf  =  snowflakes[i]
            snowflakes[i] = (sf[0] + r.randint(-1,1), sf[1] + r.randint(1,3))
            circle(surface,  pg.Color('snow1'),  (sf[0],sf[1]), r.randint(2,6))
        pg.display.flip()
        updater.tick(60)



screen,clock  = setup()
main(screen,clock)




