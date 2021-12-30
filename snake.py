import pygame as  pg

def setup() -> object:
    pg.init()
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    clock  = pg.time.Clock()
    return screen,clock




def main(surface: object, updater: object) -> None:
    done  =  False
    while not  done:
        surface.fill(pg.Color('cadetblue1'))
        for event in pg.event.get():
            if (event.type==pg.QUIT) or (event.type  ==  pg.KEYDOWN and  event.key==pg.K_ESCAPE):
                done = True
        pg.display.flip()
        updater.tick(240)



screen,clock  = setup()
main(screen,clock)




