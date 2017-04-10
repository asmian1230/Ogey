# Lee Thomas
# escaper
# Assignment 2


import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (1248, 702)   #resolution of the game
global HORIZ_MOV_INCR
HORIZ_MOV_INCR = 7          #speed of movement

global FPS
global clock
global time_spent

def RelRect(actor, camera):
    return pygame.Rect(actor.rect.x-camera.rect.x, actor.rect.y-camera.rect.y, actor.rect.w, actor.rect.h)

class Camera(object):
    '''Class for center screen on the player'''
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.center
        self.world_rect = Rect(0, 0, level_width, level_height)

    def update(self):
        
      if self.player.centerx > self.rect.centerx + 25:
          self.rect.centerx = self.player.centerx - 25
          
      if self.player.centerx < self.rect.centerx - 25:
          self.rect.centerx = self.player.centerx + 25
          
      if self.player.centery > self.rect.centery + 25:
          self.rect.centery = self.player.centery - 25
          
      if self.player.centery < self.rect.centery - 25:
          self.rect.centery = self.player.centery + 25
          
      self.rect.clamp_ip(self.world_rect)

    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, RelRect(s, self))


class Platform(pygame.sprite.Sprite):
    '''Class for create Platform'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/CorosivePlatform.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]


class Poop(pygame.sprite.Sprite):
    '''Class for creating poop'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/Poop.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

class Spikes(pygame.sprite.Sprite):
    '''Class for creating spikes'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/spikes.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

class Title(pygame.sprite.Sprite):
    '''Class for creating Title'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/Title2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

        
class Escaper(pygame.sprite.Sprite):
    '''class for player and collision'''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movy = 0
        self.movx = 0
        self.x = x
        self.y = y
        self.contact = False
        self.jump = False
        self.image = pygame.image.load('actions/ogeyRight.png').convert()
        self.image = pygame.image.load('actions/ogeyLeft.png').convert()
        self.rect = self.image.get_rect()

        self.run_left = ["actions/ogeyLeft.png","actions/ogeyLeft.png",
                         "actions/ogeyLeft.png","actions/ogeyLeft.png",
                         "actions/ogeyLeft.png","actions/ogeyLeft.png",
                         "actions/ogeyLeft.png","actions/ogeyLeft.png"]

        self.run_right = ["actions/ogeyRight.png","actions/ogeyRight.png",
                         "actions/ogeyRight.png","actions/ogeyRight.png",
                         "actions/ogeyRight.png","actions/ogeyRight.png",
                         "actions/ogeyRight.png","actions/ogeyRight.png"]

        self.direction = "right"
        self.rect.topleft = [x, y]
        self.frame = 0

    def update(self, up, down, left, right):
        if up:
            if self.contact:
                if self.direction == "right":
                    self.image = pygame.image.load("actions/ogeyRight.png")
                self.jump = True
                self.movy -= 20
        if down:
            if self.contact and self.direction == "right":
                self.image = pygame.image.load('actions/ogeyRight.png').convert_alpha()
            if self.contact and self.direction == "left":
                self.image = pygame.image.load('actions/ogeyLeft.png').convert_alpha()

        if not down and self.direction == "right":
                self.image = pygame.image.load('actions/ogeyRight.png').convert_alpha()

        if not down and self.direction == "left":
            self.image = pygame.image.load('actions/ogeyLeft.png').convert_alpha()

        if left:
            self.direction = "left"
            self.movx = -HORIZ_MOV_INCR
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.run_left[self.frame]).convert_alpha()
                if self.frame == 6: self.frame = 0
            else:
                self.image = self.image = pygame.image.load("actions/ogeyLeft.png").convert_alpha()

        if right:
            self.direction = "right"
            self.movx = +HORIZ_MOV_INCR
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.run_right[self.frame]).convert_alpha()
                if self.frame == 6: self.frame = 0
            else:
                self.image = self.image = pygame.image.load("actions/ogeyRight.png").convert_alpha()

        if not (left or right):
            self.movx = 0
        self.rect.right += self.movx

        self.collide(self.movx, 0, world)


        if not self.contact:
            self.movy += 0.3
            if self.movy > 10:
                self.movy = 10
            self.rect.top += self.movy

        if self.jump:

            self.movy += 2
            self.rect.top += self.movy
            if self.contact == True:
                self.jump = False

        self.contact = False
        self.collide(0, self.movy, world)


    def collide(self, movx, movy, world):
        self.contact = False
        for o in world:
            if self.rect.colliderect(o):
                if movx > 0:
                    self.rect.right = o.rect.left
                if movx < 0:
                    self.rect.left = o.rect.right
                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contact = True
                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0

class Level(object):
    '''Read a map and create a level'''
    def __init__(self, open_level):
        self.level1 = []
        self.world = []
        self.all_sprite = pygame.sprite.Group()
        self.level = open(open_level, "r")

    def create_level(self, x, y):
        for l in self.level:
            self.level1.append(l)

        for row in self.level1:
            for col in row:
                if col == "X":
                    corosivePlatform = Platform(x, y)
                    self.world.append(corosivePlatform)
                    self.all_sprite.add(self.world)
                if col == "M":
                    poop = Poop(x, y)
                    self.world.append(poop)
                    self.all_sprite.add(self.world)
                if col == "S":
                    spikes = Spikes(x, y)
                    self.world.append(spikes)
                    self.all_sprite.add(self.world)
                if col == "T":
                    title = Title(x, y)
                    self.world.append(title)
                    self.all_sprite.add(self.world)
                if col == "P":
                    self.escaper = Escaper(x,y)
                    self.all_sprite.add(self.escaper)
                x += 25
            y += 25
            x = 0

    def get_size(self):
        lines = self.level1
        #line = lines[0]
        line = max(lines, key=len)
        self.width = (len(line))*25
        self.height = (len(lines))*25
        return (self.width, self.height)



def tps(orologio,fps):
    temp = orologio.tick(fps)
    tps = temp / 1000.
    return tps


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()
background = pygame.image.load("world/lvl222.png").convert_alpha()
background_rect = background.get_rect()
level = Level("level/level2.txt")
level.create_level(0,0)
world = level.world
escaper = level.escaper
pygame.mouse.set_visible(0)

camera = Camera(screen, escaper.rect, level.get_size()[0], level.get_size()[1])
all_sprite = level.all_sprite

FPS = 30
clock = pygame.time.Clock()

up = down = left = right = False
x, y = 0, 0
while True:

    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_UP:
            up = True
        if event.type == KEYDOWN and event.key == K_DOWN:
            down = True
        if event.type == KEYDOWN and event.key == K_LEFT:
            left = True
        if event.type == KEYDOWN and event.key == K_RIGHT:
            right = True

        if event.type == KEYUP and event.key == K_UP:
            up = False
        if event.type == KEYUP and event.key == K_DOWN:
            down = False
        if event.type == KEYUP and event.key == K_LEFT:
            left = False
        if event.type == KEYUP and event.key == K_RIGHT:
            right = False

    asize = ((screen_rect.w // background_rect.w + 1) * background_rect.w, (screen_rect.h // background_rect.h + 1) * background_rect.h)
    bg = pygame.Surface(asize)

    for x in range(0, asize[0], background_rect.w):
        for y in range(0, asize[1], background_rect.h):
            screen.blit(background, (x, y))

    time_spent = tps(clock, FPS)
    camera.draw_sprites(screen, all_sprite)

    escaper.update(up, down, left, right)
    camera.update()
    pygame.display.flip()
