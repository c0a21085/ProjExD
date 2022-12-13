import pygame as pg
import sys

def main():
    clock = pg.time.Clock() #時間計測用オブジェクト

    pg.display.set_caption("逃げろこうかとん！") #タイトルバーに「」を表示
    scrn_sfc = pg.display.set_mode((1600, 900)) #1600x900の画面Surfaceを生成

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    #bg_sfc = pg.transform.scale(bg_sfc, (1200, 600))
    bg_rct = bg_sfc.get_rect() #Rect
    #bg_rct.center = 400, 300

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #blid  
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000) #1fpsの時を刻む
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()