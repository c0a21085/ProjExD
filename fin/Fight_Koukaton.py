import pygame as pg
import random
import sys

#画面クラス
class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

#鳥クラス
class Bird:
    key_delta = {
        pg.K_w: [0, -1],
        pg.K_s: [0, +1],
        pg.K_a: [-1, 0],
        pg.K_d: [+1, 0],
    }

    def __init__(self, img_path, ratio, x, y):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = (x, y)
        self.x = x
        self.y = y
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
            self.x = self.rct.centerx
            self.y = self.rct.centery
        self.blit(scr)                    

    def koukaton_update(self, press_key, scr:Screen): #こうかとんの画像のアップデート
        self.sfc = pg.image.load(f"fig/{press_key}.png") #押したキー(0~9)に対応した画像を読み込む
        self.sfc = pg.transform.rotozoom(self.sfc, 0, self.ratio) #サイズは初期状態と同じ
        self.rct = self.sfc.get_rect()
        self.rct.center = (self.x, self.y) #こうかとんの現在地に座標を合わせる 
        self.blit(scr)

    def get_bird_point(self):
        return (self.x, self.y)

#爆弾クラス
class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) 
        self.sfc.set_colorkey((0, 0, 0))
        self.rad = rad 
        self.color = color
        pg.draw.circle(self.sfc, self.color, (self.rad, self.rad), self.rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.x = self.rct.centerx
        self.y = self.rct.centery
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.x += self.vx
        self.y += self.vy
        self.blit(scr)

    def speed_update(self, press_key): #速度のアップデート
        base_speed = 0.5
        #上キーを押すと(速度が早くなる)
        if press_key == pg.K_UP and self.vx > 0 and self.vy > 0: #x方向：正,y方向：正 
            self.vx += base_speed
            self.vy += base_speed
        elif press_key == pg.K_UP and self.vx > 0 and self.vy < 0: #x方向：正,y方向：負
            self.vx += base_speed
            self.vy -= base_speed
        elif press_key == pg.K_UP and self.vx < 0 and self.vy > 0: #x方向：負,y方向：正 
            self.vx -= base_speed
            self.vy += base_speed
        elif press_key == pg.K_UP and self.vx < 0 and self.vy < 0: #x方向：負,y方向：負 
            self.vx -= base_speed
            self.vy -= base_speed
        elif press_key == pg.K_UP and self.vx == 0 and self.vy == 0: #動いていない場合
            self.vx += base_speed*random.choice([-1, 1])
            self.vy += base_speed*random.choice([-1, 1])
        #下キーを押すと、かつ速度の絶対値が0よりも大きければ(速度が遅くなる)３ｗ
        if press_key == pg.K_DOWN and abs(self.vx) > 0 and abs(self.vy) > 0:
            if self.vx > 0 and self.vy > 0: #x方向：正,y方向：正 
                self.vx -= base_speed
                self.vy -= base_speed
            elif self.vx > 0 and self.vy < 0: #x方向：正,y方向：負 
                self.vx -= base_speed
                self.vy += base_speed
            elif self.vx < 0 and self.vy > 0: #x方向：負,y方向：正
                self.vx += base_speed
                self.vy -= base_speed
            elif self.vx < 0 and self.vy < 0:#x方向：負,y方向：負 
                self.vx += base_speed
                self.vy += base_speed
    
    def size_update(self, press_key, scr:Screen): #サイズのアップデート
        #右キーを押す、かつ半径が0以上ならば(サイズが大きくなる)
        if press_key == pg.K_RIGHT and self.rad >= 0:
            self.rad += 6
        #左キーを押す、かつ半径が初期値よりも大きいならば(サイズが小さくなる)
        if press_key == pg.K_LEFT and self.rad > 6:
            self.rad -= 6 
        self.sfc = pg.Surface((2*self.rad, 2*self.rad)) 
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, self.color, (self.rad, self.rad), self.rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = self.x
        self.rct.centery = self.y
        self.vx = random.choice([-1, +1])
        self.vy = random.choice([-1, +1])
        self.blit(scr) 

#銃クラス
class Bullet():
    def __init__(self, color, rad, vxy, xy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) 
        self.sfc.set_colorkey((0, 0, 0))
        self.rad = rad 
        self.color = color
        pg.draw.circle(self.sfc, self.color, xy, self.rad)
        self.rct = self.sfc.get_rect()
        self.x, self.y = xy
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        self.blit(scr)
    

#Scoreクラス
class Score():
    def __init__(self, bomb:Bomb):
        self.score = 0
        self.font = pg.font.Font(None, 60)
        self.color = (0, 0, 0)
    
    def update(self, bomb:Bomb):
        self.score += (abs(bomb.vx) / 100) * (bomb.rad / 10) #Scoreの加算

    def get_score(self):
        return int(self.score)

    def blit(self, scr:Screen):
        scr.sfc.blit(self.text, (50, 50))

    def result(self, scr:Screen):
        self.text = self.font.render(f"Score:{int(self.score)}", True, self.color)   # 描画する文字列の設定
        self.blit(scr)
    

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
    scr = Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")

    bird = Bird("fig/6.png", 2.0, 900, 400)
    bird.update(scr)

    bomb_list = []
    for i in range(5):
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1]) 
        bomb = Bomb((255, 0, 0), 6*random.randint(1,5), (vx, vy), scr)
        bomb_list.append(bomb)
    bomb.update(scr)

    bullet_list = []

    SpeedKey_list = [pg.K_UP, pg.K_DOWN] #速度調整用キー
    SizeKey_list = [pg.K_RIGHT, pg.K_LEFT] #サイズ調整用キー
    KoukatonKey_list = [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9] #画像変更用キー
    score = Score(bomb) #Scoreの算出

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
                        bakudan.size_update(press_key, scr) #それぞれの爆弾のサイズを変更
                if press_key in KoukatonKey_list: #押されたキーがこうかとんの画像変更用キーならば
                    for num in range(len(KoukatonKey_list)):
                        if press_key == KoukatonKey_list[num]:
                            bird.koukaton_update(num, scr)
                if press_key == pg.K_BACKSPACE:
                    bullet = Bullet((0, 0, 255), 5, (1, 1), (bird.x, bird.y), scr)
                    bullet_list.append(bullet)

        bird.update(scr)
        for bakudan in bomb_list:
            bakudan.update(scr)
            if bird.rct.colliderect(bakudan.rct):
                print(f"最終スコア：{score.get_score()}")
                return
            for tama in bullet_list:
                if tama.rct.colliderect(bakudan.rct):
                    return 
                
        score.update(bomb)
        score.result(scr)
        pg.display.update()
        clock.tick(1000)
 

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()