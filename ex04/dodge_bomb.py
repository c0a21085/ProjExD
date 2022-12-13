import pygame as pg
import sys
from random import randint

def check_bound(obj_rct ,scr_rct):
    yoko,tate = 1, 1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def main():
    clock = pg.time.Clock() #時間計測用オブジェクト

    #画面と背景
    pg.display.set_caption("逃げろこうかとん！") #タイトルバーに「」を表示
    scrn_sfc = pg.display.set_mode((1600, 900)) #1600x900の画面Surfaceを生成
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect() #Rect

    #プレイヤー(こうかとん)
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) #blid  

    #爆弾
    bomb_sfc = pg.Surface((100, 100))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (50, 50), 10) 
    bomb_rct = bomb_sfc.get_rect() 
    bomb_rct.centerx = randint(0,scrn_sfc.get_width())
    bomb_rct.centery = randint(0,scrn_sfc.get_height()) 
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = 1, 1

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #blid
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN: #キーが押されたとき
                if event.key == pg.K_UP: #↑キーが押されたら
                    if vx >= 0: #x方向の速さが正だったら
                        vx += 1 
                    else:       #x方向の速さが負だったら
                        vx -= 1
                    if vy >= 0: #y方向の速さが正だったら
                        vy += 1
                    else:       #y方向の速さが正だったら
                        vy -= 1
                if event.key == pg.K_DOWN: #↓キーが押されたら
                    if abs(vx) > 0 and abs(vy) > 0: #x,y方向の速さの絶対値が0より大きければ
                        if vx >= 0: #x方向の速さが正だったら
                            vx -= 1 
                        else:       #x方向の速さが負だったら
                            vx += 1
                        if vy >= 0: #y方向の速さが正だったら
                            vy -= 1
                        else:       #y方向の速さが正だったら
                            vy += 1 
        bomb_rct.move_ip(vx, vy) 
        scrn_sfc.blit(bomb_sfc, bomb_rct)             
            
        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_w]:
            tori_rct.centery -= 1
        if key_dict[pg.K_s]:
            tori_rct.centery += 1
        if key_dict[pg.K_d]:
            tori_rct.centerx += 1
        if key_dict[pg.K_a]:
            tori_rct.centerx -= 1
        if check_bound(tori_rct, scrn_rct) != (1, 1):
            if key_dict[pg.K_w]:
                tori_rct.centery += 1
            if key_dict[pg.K_s]:
                tori_rct.centery -= 1
            if key_dict[pg.K_d]:
                tori_rct.centerx -= 1
            if key_dict[pg.K_a]:
                tori_rct.centerx += 1 
        scrn_sfc.blit(tori_sfc, tori_rct)

        #bomb_rct.move_ip(vx, vy)
        #scrn_sfc.blit(bomb_sfc, bomb_rct)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        if tori_rct.colliderect(bomb_rct):
            return
        print(vx, vy)

        pg.display.update()
        clock.tick(1000) #1000fpsの時を刻む
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()