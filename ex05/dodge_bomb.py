import pygame as pg
import random
import sys

key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}

class Screen:
    def __init__(self, title = "逃げろ！こうかとん", size = (1600, 900), image = "fig/pg_bg.jpg"):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(image)
        self.bgi_rct = self.bgi_sfc.get_rect()  

    def blid(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 
        

class Bird():
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }   

    def __init__(self, image = "fig/6.png", ratio = 2.0, xy = (900, 400)):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blid(self, scr:Screen):
        scr.sfc.blid(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, self.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blid(scr)


class Bomb():
    def __init__(self, color = (255, 0, 0), rad = 10, vxy = (+1, +1)):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, self.rct.width)
        self.rct.centery = random.randint(0, self.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blid(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        scr.sfc.blit(self.sfc, self.rct) 
        yoko, tate = check_bound(self.rct, self.rct)
        vx *= yoko
        vy *= tate


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
    
    scr = Screen()

    bird = Bird()
    bird.update(scr)

    bomb = Bomb()
    bomb.update(scr)

    # 練習２
    while True:
        scr.blid()
  
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        bird.update(scr)
        bomb.update(scr)       
        if bird.rct.colliderect(bomb.rct):
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()