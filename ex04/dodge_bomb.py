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

def make_bomb(obj_sfc, obj_rct, scr_sfc):
    pg.draw.circle(obj_sfc, (255, 0, 0), (50, 50), 10) 
    obj_rct.centerx = randint(0,scr_sfc.get_width())
    obj_rct.centery = randint(0,scr_sfc.get_height()) 
    scr_sfc.blit(obj_sfc, obj_rct) 

def koukaton_change(obj_sfc):
    obj_sfc = pg.image.load("fig/5.png")

def main():
    clock = pg.time.Clock() #時間計測用オブジェクト
    time = 0
    #score = time // 1000

    #画面と背景
    #pg.display.set_caption(f"逃げろこうかとん！  Score：{time}") 
    pg.display.set_caption(f"逃げろこうかとん！") #タイトルバーに「」を表示
    scrn_sfc = pg.display.set_mode((1600, 900)) #1600x900の画面Surfaceを生成
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect() #Rect

    #プレイヤー(こうかとん)
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc,0, 1.5)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) #blid  

    #爆弾
    bomb_sfc = pg.Surface((100, 100))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (40, 40), 40)
    bomb_rct = bomb_sfc.get_rect() 
    bomb_rct.centerx = randint(0,scrn_sfc.get_width())
    bomb_rct.centery = randint(0,scrn_sfc.get_height())
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = 1, 1
    font = pg.font.Font(None, 60)
    add = abs(vx)

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
                    add += 1
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
                        add -= 1
                if event.key == pg.K_RIGHT: #→キーが押されたら
                    #width += 10
                    pass
                if event.key == pg.K_LEFT: #←キーが押されたら
                    if abs(vx) > 0 and abs(vy) > 0: #x,y方向の速さの絶対値が0より大きければ
                        if vx >= 0: #x方向の速さが正だったら
                            vx -= 1 
                        else:       #x方向の速さが負だったら
                            vx += 1
                if event.key == pg.K_KP_ENTER:
                    #make_bomb(bomb_sfc, bomb_rct, scrn_sfc)
                    #koukaton_change(tori_sfc)
                    pass    

        bomb_rct.move_ip(vx, vy) 
        #bomb_rct.inflate_ip(width)
        scrn_sfc.blit(bomb_sfc, bomb_rct)             
            
        #キー操作
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

        #爆弾の跳ね返り
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        if tori_rct.colliderect(bomb_rct):
            return 

        time += add
        score = time // 200
        text = font.render(f"Score:{score}", True, (0,0,0))   # 描画する文字列の設定
        scrn_sfc.blit(text, [50, 50])# 文字列の表示位置
        pg.display.update()
        clock.tick(1000) #1000fpsの時を刻む
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()