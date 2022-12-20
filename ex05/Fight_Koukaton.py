import pygame as pg
import random
import sys


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_w: [0, -1],
        pg.K_s: [0, +1],
        pg.K_a: [-1, 0],
        pg.K_d: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.ratio = ratio

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    

    def koukaton_update(self, press_key, scr:Screen):
        self.sfc = pg.image.load(f"fig/{press_key}.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, self.ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = self.x, self.y  
        self.blit(scr)


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) 
        self.sfc.set_colorkey((0, 0, 0))
        self.rad = rad
        pg.draw.circle(self.sfc, color, (self.rad, self.rad), self.rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.rct.fit(self.rct)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

    def speed_update(self, press_key): #速度のアップデート
        #上キーを押すと(速度が早くなる)
        if press_key == pg.K_UP and self.vx >= 0 and self.vy >= 0: #x方向：正,y方向：正 
            self.vx += 1
            self.vy += 1
        elif press_key == pg.K_UP and self.vx >= 0 and self.vy <= 0: #x方向：正,y方向：負
            self.vx += 1
            self.vy -= 1
        elif press_key == pg.K_UP and self.vx <= 0 and self.vy >= 0: #x方向：負,y方向：正 
            self.vx -= 1
            self.vy += 1
        elif press_key == pg.K_UP and self.vx <= 0 and self.vy <= 0: #x方向：負,y方向：負 
            self.vx -= 1
            self.vy -= 1        
        #下キーを押すと、かつ速度の絶対値が0よりも大きければ(速度が遅くなる)
        if press_key == pg.K_DOWN and abs(self.vx) > 0 and abs(self.vy) > 0:
            if self.vx > 0 and self.vy > 0: #x方向：正,y方向：正 
                self.vx -= 1
                self.vy -= 1
            elif self.vx > 0 and self.vy < 0: #x方向：正,y方向：負 
                self.vx -= 1
                self.vy += 1
            elif self.vx < 0 and self.vy > 0: #x方向：負,y方向：正
                self.vx += 1
                self.vy -= 1
            elif self.vx < 0 and self.vy < 0:#x方向：負,y方向：負 
                self.vx += 1
                self.vy += 1
    
    def size_update(self, press_key): #サイズのアップデート
        #右キーを押す、かつ半径が0以上ならば(サイズが大きくなる)
        if press_key == pg.K_RIGHT and self.rad >= 0:
            self.rad += 10
        #左キーを押す、かつ半径が0よりも大きいならば(サイズが小さくなる)
        if press_key == pg.K_LEFT and self.rad > 0:
            self.rad -= 10  



def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()

    scr = Screen("負けるな！こうかとん", (1200,700), "fig/pg_bg.jpg")

    bird = Bird("fig/6.png", 2.0, (900,400))
    bird.update(scr)

    bomb_list = []
    for i in range(2):
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1]) 
        bomb = Bomb((255, 0, 0), 10, (vx, vy), scr)
        bomb_list.append(bomb)
    #bomb.update(scr)

    SpeedKey_list = [pg.K_UP, pg.K_DOWN]
    SizeKey_list = [pg.K_RIGHT, pg.K_LEFT]
    KoukatonKey_list = [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN: #キーが押されたら
                press_key = event.key 
                if press_key in SpeedKey_list: #押されたキーが速度調整用のキーならば
                    for bakudan in bomb_list:
                        bakudan.speed_update(press_key) #それぞれの爆弾のスピードを変更
                if press_key in SizeKey_list: #押されたキーがサイズ調整用のキーならば
                    for bakudan in bomb_list:
                        bakudan.size_update(press_key) #それぞれの爆弾のサイズを変更
                if press_key in KoukatonKey_list: #押されたキーがこうかとんの画像変更用キーならば
                    for num in range(len(KoukatonKey_list)):
                        if press_key == KoukatonKey_list[num]:
                            bird.koukaton_update(num, scr)

        bird.update(scr)
        for bakudan in bomb_list:
            bakudan.update(scr)
            if bird.rct.colliderect(bakudan.rct):
                return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()