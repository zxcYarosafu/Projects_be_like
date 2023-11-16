
import sys
import os
from random import *
from time import time as timer
nl = 10
from pygame import *
window = display.set_mode((700,500))
display.set_caption("Астероїди")
w    , h = 700,500
fps = 100
back = (255,255,255)
background = transform.scale(image.load('pict/galaxy.jpg'),(w,h))
clock = time.Clock()
score = 0
game = True
finish = False
font.init()
mainfont = font.Font( None, 26)
lose = mainfont.render("Your ship is broken", True, (255, 0, 0))
bl = 100
ll = 100
haste = 7.5
haste1 = 1
haste3 = 2
reload_time = False
num_fire = 0


bs = 25

class GameSprite(sprite.Sprite):

    def __init__(self,pImage,pX,pY,sizeX,sizeY,pSpeed):
        super().__init__()
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.image = transform.scale(image.load(pImage),(self.sizeX,self.sizeY))
        self.speed = pSpeed
        self.rect = self.image.get_rect()
        self.rect.x = pX
        self.rect.y = pY

    def draw(self):
        window.blit(self.image ,(self.rect.x,self.rect.y))


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed


    def fire(self):

        bullet = Bullet("pict/bullet.png", self.rect.centerx - 6, self.rect.top, 15, 30, 15)
        bullets.add(bullet)




ship1 = 'skins/noskin.png'






ship = Hero(ship1 , 100 , 420 , 60 , 80 , haste)
bullets = sprite.Group()
lost = 0
# if keys[K_f]:
class Enemy(GameSprite):
    def update(self):
        global lost, hearts
        self.rect.y += self.speed
        if self.rect.y > h:
            try:
                hearts.pop(0)
            except:
                pass
            self.rect.y = - 50
            self.rect.x = randint(0,700)
            lost += 1

    def speed_up(self):
        self.speed += 1

    def boss_move(self, xspeed):
        self.rect.x += xspeed
        self.rect.y += 1
        if self.rect.x <= w-100:
            #xspeed *= -1
            if self.rect.y > h:
                try:
                    for i in range(3):
                        hearts.pop()
                except:
                    pass

mixer.init()
mixer.music.load("pict/adv.ogg")
mixer.music.play(1000000)
mixer.music.set_volume(0)
fire_sound = mixer.Sound("pict/gun.wav")
asteroids = sprite.Group()


for i in range (5):
    asteroid = Enemy('pict/asteroid.png',randint(0,700),-150,70 ,70 ,1)
    asteroids.add(asteroid)

hearts = []
lives = 5
x = 315

boss = Enemy('pict/ufos.jfif' , randint(0 , 600) , 0 , 256 ,128 , randint(1 , 4))

for i in range(lives):
    heart = GameSprite('pict/heart.png' , x ,5 , 30 , 30 , 0)
    hearts.append(heart)
    x += 15

dont = mainfont.render("Choose the ship", True, (255, 0, 0))

name = mainfont.render("Ship Adventury", True, (255, 0, 0))



restart = GameSprite("butt/restart.png" , 250 , 220 , 170 , 70 , 0)

start = GameSprite('butt/start.png' , 0 , 80 , 320 , 140 , 0)

selected1 = GameSprite('skins/noskin.png' , 275 , 100 , 130 , 130 , 0 )

exit_button = GameSprite('butt/exit.png' , 35 , 380 , 120 ,  80 , 0 )

skins_button = GameSprite('butt/skin.png' , 50, 280 , 80 , 65 , 0)

skin_n = mainfont.render("Skin changer", True, (255, 0, 0))

finish = True

not_ch = False

menu = True

bt_lf = GameSprite('butt/left.png', 100 , 100 , 112 , 112 , 0)

bt_rg = GameSprite('butt/right.png', 500 , 100 , 112 , 112 , 0)

ships = False

select1 = GameSprite('skins/ship1.png', 100 , 350 , 60 , 80 , 0)
select2 = GameSprite('skins/ship2.png', 300 , 350 , 60 , 80 , 0)
select3 = GameSprite('skins/ship3.png', 500 , 350 , 60 , 80 , 0)

back_to_menu = False

exit_to_mn = GameSprite('butt/exit.png' , 580 , 0 , 120 ,  80 , 0 )

ship_lives = 3

skin_sh = False

while game:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_f:
                if num_fire < randint(10,35) and reload_time == False and not menu:
                    ship.fire()
                    fire_sound.play()
                    fire_sound.set_volume(0.1)
                    num_fire += 1
                if num_fire >= 20 and reload_time == False:
                    reload_start = timer()
                    reload_time = True
            if e.key == K_q:
                score += 99
            if e.key == K_k:
                hearts.remove(heart )
            if e.key == K_r:
                reload_start = timer()
                reload_time = True
            if e.key == K_o:
                ship.image = transform.scale(image.load('skins/ship1.png'), (60, 90))
                ship.rect.y = 400
            if e.key == K_p:
                ship.image = transform.scale(image.load('skins/ship2.png'), (60 , 90))
            if e.key == K_i:
                background = transform.scale(image.load('pict/galaxy 2.jfif'), (700 , 500))

        if e.type == QUIT:
            game = False



        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x,y = e.pos
                if restart.rect.collidepoint(x,y) and finish and back_to_menu :
                    for a in asteroids:
                        a.rect.x = randint(0 , 600 )
                        a.rect.y = randint(-60 , -40)
                    score , lost , finish , num_fire = 0 , 0 , 0 , 0
                    hearts = []
                    lives = 5
                    x = 315

                    for i in range(lives):
                        heart = GameSprite('pict/heart.png', x, 5, 30, 30, 0)
                        hearts.append(heart)
                        x += 15
                if exit_to_mn.rect.collidepoint(x,y):
                    back_to_menu = False
                    menu = True
                    skin_sh = True
                if start.rect.collidepoint(x, y) and skin_sh:
                    menu = True
                    finish = True
                if restart.rect.collidepoint(x, y) and finish and not back_to_menu:
                    finish = False
                    menu = False
                    back_to_menu = True
                if exit_button.rect.collidepoint(x , y) and skin_sh:
                    game = False
                if skins_button.rect.collidepoint(x , y ):
                    menu = False
                    skin_sh = False
                if select1.rect.collidepoint(x,y):
                    menu = False
                    skin_sh = False
                    selected1.image = transform.scale(image.load('skins/ship1.png'), (60, 80))
                    ship.image = transform.scale(image.load('skins/ship1.png'), (60, 80))
                    ships = True
                if select2.rect.collidepoint(x,y):
                    menu = False
                    skin_sh = False
                    selected1.image = transform.scale(image.load('skins/ship2.png'), (60, 80))
                    ship.image = transform.scale(image.load('skins/ship2.png'), (60, 80))
                    ships = True
                if select3.rect.collidepoint(x,y):
                    menu = False
                    skin_sh = False
                    selected1.image = transform.scale(image.load('skins/ship3.png'), (60, 80))
                    ship.image = transform.scale(image.load('skins/ship3.png'), (60, 80))
                    ships = True

    if not skin_sh and not menu:
        window.blit(background, (0, 0))
        exit_to_mn.draw()
        selected1.draw()
        select1.draw()
        select2.draw()
        select3.draw()





    if menu:
        window.blit(background, (0, 0))
        window.blit(skin_n, (40, 250))
        start.draw()
        exit_button.draw()
        skins_button.draw()
        if not_ch:
            window.blit(dont ,(400, 300) )

    if not finish :
        if  ships:
            window.blit(background, (0, 0))
            #
            missed = mainfont.render("MISSED: " + str(lost), True, (255, 155, 55))
            killed = mainfont.render("KILLED: " + str(score), True, (255, 155, 55))
            window.blit(missed, (5, 10))
            window.blit(killed, (5, 50))


            if score >= bs :
                pass
                #boss.draw()
                #boss.boss_move(randint(1 , 1))
                #bs += 25
                #if boss.rect.x >= 450 :
                    #pass

            ship.draw()
            ship.update()

            asteroids.update()
            asteroids.draw(window)

            bullets.update()
            bullets.draw(window)
            collides = sprite.groupcollide(bullets, asteroids, True, True)
            for heart in hearts:
                heart.draw()
            for c in collides:
                score += 1
                asteroid = Enemy("pict/asteroid.png", randint(0, 600), -50, 70, 70, randint(haste1, haste3))
                asteroids.add(asteroid)
            if ship.rect.x >= 640:
                ship.rect.x = 640
            if ship.rect.x <= 0:
                ship.rect.x = 0
            if reload_time:
                reload_end = timer()
                if reload_end - reload_start < randint(1,5):
                    msg_reload = mainfont.render('Recharging.' ,True, (0 , 200 , 0) )

                    window.blit(msg_reload , (250,250))
                else:
                    num_fire = 0
                    reload_time = False

            if sprite.spritecollide(ship, asteroids , False):
                finish = True
                window.blit(lose, (250, 200))
                exit_to_mn.draw()
                restart.draw()


            if len(hearts) == 0 and back_to_menu  :


                window.blit(lose , (250 , 200))
                exit_to_mn.draw()
                restart.draw()
                finish = True

    display.update()
    clock.tick(60)


