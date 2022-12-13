import pygame as pg
import sys
from random import randint

def main():
    clock = pg.time.Clock() #時間計測用オブジェクト

    pg.display.set_caption("逃げろこうかとん！") #タイトルバーに「」を表示
    scrn_sfc = pg.display.set_mode((1400, 800)) #1600x900の画面Surfaceを生成

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect() #Rect

    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400

    draw_sfc = pg.Surface((100, 100))
    draw_sfc.set_colorkey((0, 0, 0))
     
    x_point = randint(0,scrn_sfc.get_width())
    y_point = randint(0,scrn_sfc.get_height()) 
    pg.draw.circle(draw_sfc, (255, 0, 0), (50, 50), 10) 


    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #blid
        scrn_sfc.blit(tori_sfc, tori_rct) #blid 
        scrn_sfc.blit(draw_sfc, (x_point, y_point))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1

        x_point += 1
        y_point += 1

        pg.display.update()
        clock.tick(1000) #1000fpsの時を刻む
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()