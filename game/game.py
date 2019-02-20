#import libraries
import pygame as pg
from pygame.locals import *
from random import *
from spritesheet_functions import SpriteSheet
from threading import *
import sys, time, math, os

#initiate pygame
pg.init()

#set up display to standard hd pixel count/ratio at fullscreen
screen = pg.display.set_mode((1280, 720), pg.FULLSCREEN)
pg.display.set_caption("Endless Boss")

#set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')


#load spritesheets
ss_tank = 'gunner sprite sheet.png'
ss_eyeBoss = 'eye sprite sheet.png'
ss_laser = 'laser sprite sheet.png'

#load sidebar images
sb_player = pg.image.load('Player Side.png')
sb_boss = pg.image.load('Boss Side.png')

#load backgrounds
bg_stars = pg.image.load('bg_stars.jpg')
bg_stars = pg.transform.scale(bg_stars, (1366, 768))

#rotate on center function
def rotate(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pg.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

#Threaded timer class (found on stack overflow from MestreLion)
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

#collision detection function
def collisionDetect(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    if x1 > x2 and x1 < x2 + w2 or x1 + w1 > x2 and x1 + w1 < x2 + w2:
        if y1 > y2 and y1 < y2 + h2 or y1 + h1 > y2 and y1 + h1 < y2 + h2:
            return True

#Character Class
class character:
    def __init__(self, sprite, health, damage):

        self.maxHP, self.health, self.damage = float(health), float(health), damage

        self.position = 2

        self.ss = SpriteSheet(sprite)
        xL, yL = 0, 0
        self.images = []
        for i in range(5):
            self.image = self.ss.get_image(xL, yL, 128, 128)
            self.images.append(self.image)
            xL += 128

        self.active = False
        self.im = 0
        self.animation = False

    def event_handle(self, event):
        if event.type == pg.KEYDOWN:
            #movement events
            if self.active == False and self.animation == False:
                if event.key == pg.K_UP:
                    if self.position == 4:
                        self.position = 1
                    elif self.position == 5:
                        self.position = 3
                    elif self.position == 6:
                        self.position = 4
                    elif self.position == 8:
                        self.position = 5
                if event.key == pg.K_LEFT:
                    if self.position == 2:
                        self.position = 1
                    elif self.position == 3:
                        self.position = 2
                    elif self.position == 7:
                        self.position = 6
                    elif self.position == 8:
                        self.position = 7
                if event.key == pg.K_DOWN:
                    if self.position == 1:
                        self.position = 4
                    elif self.position == 3:
                        self.position = 5
                    elif self.position == 4:
                        self.position = 6
                    elif self.position == 5:
                        self.position = 8
                if event.key == pg.K_RIGHT:
                    if self.position == 1:
                        self.position = 2
                    elif self.position == 2:
                        self.position = 3
                    elif self.position == 6:
                        self.position = 7
                    elif self.position == 7:
                        self.position = 8
                if event.key == pg.K_SPACE:
                    self.animation = True
                    boss.health = boss.health - self.damage
                    print boss.health

    def draw(self, screen):
        w = screen.get_width()
        h = screen.get_height()

        image = self.images[self.im]

        if self.position == 1:
            self.rect = posOne.rect
            image = rotate(image, 45)

        if self.position == 2:
            self.rect = (((int(w)/2)-64), ((int(h)/2)-256), 128, 128)

        if self.position == 3:
            self.rect = posThree.rect
            image = rotate(image, 315)

        if self.position == 4:
            self.rect = posFour.rect
            image = rotate(image, 90)

        if self.position == 5:
            self.rect = posFive.rect
            image = rotate(image, 270)

        if self.position == 6:
            self.rect = posSix.rect
            image = rotate(image, 135)

        if self.position == 7:
            self.rect = posSeven.rect
            image = rotate(image, 180)

        if self.position == 8:
            self.rect = posEight.rect
            image = rotate(image, 225)

        screen.blit(image, self.rect)
        if self.animation == True:
            if self.im < 4:
                self.im = self.im + 1
            else:
                self.im = 0
                self.animation = False
        screen.blit(sb_player, (0, 0, 0, 0))
        pg.draw.rect(screen, WHITE, (128, 96, 96, h - 192), 0)
        pg.draw.rect(screen, RED, (144, h-128-((h - 256)*(self.health/self.maxHP)), 64, (h - 256)*(self.health/self.maxHP)), 0)

#Boss Class
class Boss:
    def __init__(self, x, y, w, h, screen):
        #set up health, damage, attacks
        self.health = float(randint(150, 300))
        self.maxHP = self.health
        self.damage = randint(10, 50)
        self.attacks = []

        #set up sprite and rect values
        self.rect = (x, y, w, h)
        image = rndSprite()
        self.ss = SpriteSheet(ss_eyeBoss)
        xL, yL = 0, 0
        self.images = []
        if image == ss_eyeBoss:
            rng = 16
            self.num = 16
        for i in range(rng):
            self.image = self.ss.get_image(xL, yL, 128, 128)
            self.images.append(self.image)
            xL = xL + 128
        self.im = 0

        #abilities set up
        self.que = []
        self.abilityNum = 0
        self.las = False
        useAbility = RepeatedTimer(0.5, self.attack, screen)
        addLaser = RepeatedTimer(0.5, self.addQue, "laser")

    def attack(self, screen):
        if self.que[0] == "laser":
           self.las = True
        self.que.pop(0)

    def addQue(self, ability):
        if ability == "laser":
            self.que.append("laser")

    def draw(self, screen):
        if self.health > 0:
            w = int(screen.get_width())
            h = int(screen.get_height())

            image = self.images[self.im]

            if player.position == 1:
                image = rotate(image, 45)

            if player.position == 3:
                image = rotate(image, 315)

            if player.position == 4:
                image = rotate(image, 90)

            if player.position == 5:
                image = rotate(image, 270)

            if player.position == 6:
                image = rotate(image, 135)

            if player.position == 7:
                image = rotate(image, 180)

            if player.position == 8:
                image = rotate(image, 225)

            screen.blit(image, self.rect)
            if self.im < self.num - 1:
                self.im = self.im + 1

            #health bar
            screen.blit(sb_boss, (w-352, 0, 0, 0))
            pg.draw.rect(screen, WHITE, (w - (144 + 64), 96, 96, h - 192), 0)
            pg.draw.rect(screen, RED, (w - (128 + 64), h-128-((h - 256)*(self.health/self.maxHP)), 64, (h - 256)*(self.health/self.maxHP)), 0)

#function to select a random boss sprite
def rndSprite():
    bossSprites = [ss_eyeBoss]
    sprite = choice(bossSprites)
    return sprite

#class for laser boss shoots
class laser:
    def __init__(self):
        #set up rect
        w = int(screen.get_width())
        h = int(screen.get_height())
        self.rect = ((w-32)/2, (h-16)/2, 32, 32)

        #set up sprites
        self.ss = SpriteSheet(ss_laser)
        xL, yL = 0, 0
        self.images = []
        for i in range(11):
            self.image = self.ss.get_image(xL, yL, 32, 32)
            self.images.append(self.image)
            xL += 32
        self.active = False
        self.im = 0
        self.animation = False

        #set up speed and direction
        if player.position == 1:
            self.xSpeed = -math.sqrt(200)
            self.ySpeed = -math.sqrt(200)
        if player.position == 2:
            self.xSpeed = 0
            self.ySpeed = -20
        if player.position == 3:
            self.xSpeed = math.sqrt(200)
            self.ySpeed = -math.sqrt(200)
        if player.position == 4:
            self.xSpeed = -20
            self.ySpeed = 0
        if player.position == 5:
            self.xSpeed = 20
            self.ySpeed = 0
        if player.position == 6:
            self.xSpeed = -math.sqrt(200)
            self.ySpeed = math.sqrt(200)
        if player.position == 7:
            self.xSpeed = 0
            self.ySpeed = 20
        if player.position == 8:
            self.xSpeed = math.sqrt(200)
            self.ySpeed = math.sqrt(200)

        #set up damage
        self.damaged = False

    def draw(self, screen):
        if self.active == False:
            self.active = True
            self.image = self.images[self.im]
            if player.position == 1:
                self.image = rotate(self.image, 135)
            if player.position == 2:
                self.image = rotate(self.image, 90)
            if player.position == 3:
                self.image = rotate(self.image, 45)
            if player.position == 4:
                self.image = rotate(self.image, 180)
            if player.position == 6:
                self.image = rotate(self.image, 225)
            if player.position == 7:
                self.image = rotate(self.image, 270)
            if player.position == 8:
                self.image = rotate(self.image, 315)
        if not collisionDetect(self.rect, player.rect):
            x, y, w, h = self.rect
            x += self.xSpeed
            y += self.ySpeed
            self.rect = x, y, w, h
        elif self.im < 10:
            if not self.damaged:
                player.health -= 10
                self.damaged = True
            self.im += 1
            self.image = self.images[self.im]
            if player.position == 1:
                self.image = rotate(self.image, 135)
            if player.position == 2:
                self.image = rotate(self.image, 90)
            if player.position == 3:
                self.image = rotate(self.image, 45)
            if player.position == 4:
                self.image = rotate(self.image, 180)
            if player.position == 6:
                self.image = rotate(self.image, 225)
            if player.position == 7:
                self.image = rotate(self.image, 270)
            if player.position == 8:
                self.image = rotate(self.image, 315)

        screen.blit(self.image, self.rect)

#platform class
class platform:
    def __init__(self, x, y, w, h):
        self.rect = (x, y, w, h)
        xL = 0
        yL = 0
        self.ss = SpriteSheet("colors.png")
        self.images = []
        for i in range(2):
            self.image = self.ss.get_image(xL, yL, 128, 128)
            self.images.append(self.image)
            xL = xL + 128
        xL = 0
        yL = 128
        for i in range(1):
            self.image = self.ss.get_image(xL, yL, 128, 128)
            self.images.append(self.image)
            xL = xL + 128
        self.sprite = choice(self.images)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

#state switch button class


#Variable setup
w = screen.get_width()
h = screen.get_height()

clock = pg.time.Clock()

done = False
state = "fight"

#Main loop
while True:
    #if state == "start":

    if state == "fight":
        posOne = platform(((int(w)/2)-256), ((int(h)/2)-256), 128, 128)
        posTwo = platform(((int(w)/2)-64), ((int(h)/2)-256), 128, 128)
        posThree = platform(((int(w)/2)+128), ((int(h)/2)-256), 128, 128)
        posFour = platform(((int(w)/2)-256), ((int(h)/2)-64), 128, 128)
        posFive = platform(((int(w)/2)+128), ((int(h)/2)-64), 128, 128)
        posSix = platform(((int(w)/2)-256), ((int(h)/2)+128), 128, 128)
        posSeven = platform(((int(w)/2)-64), ((int(h)/2)+128), 128, 128)
        posEight = platform(((int(w)/2)+128), ((int(h)/2)+128), 128, 128)
        platforms = [posOne, posTwo, posThree, posFour, posFive, posSix, posSeven, posEight]

        player = character(ss_tank, 100, 10)

        boss = Boss(((int(w)/2)-64), ((int(h)/2)-64), 128, 128, screen)
        drawAttacks = []
        while state == "fight":
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                    os._exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                        os._exit()
                player.event_handle(event)
            screen.blit(bg_stars, (0, 0, 0, 0))
            for plat in platforms:
                plat.draw(screen)
            if player.health > 0:
                player.draw(screen)
                print player.health
                if boss.health > 0:
                    boss.draw(screen)
                    if boss.las == True:
                        globals()["laser%s" % str(boss.abilityNum)] = laser()
                        drawAttacks.append(globals()["laser%s" % str(boss.abilityNum)])
                        boss.abilityNum += 1
                        boss.las = False
                    for da in drawAttacks:
                        da.draw(screen)
            pg.display.update()     #updates screen
            pg.display.flip()       #updates display
            clock.tick(30)          #game fps
