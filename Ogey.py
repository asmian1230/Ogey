import pygame, sys
from pygame.locals import *

SCREEN_SIZE = (800, 480)

#Camera to center around player
class Camera(object):
    
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

#Creates initial game state
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
screen_rect = screen.get_rect()
background = pygame.image.load("L1/background.png").convert_alpha()
background_rect = background.get_rect()


FPS = 60
clock = pygame.time.Clock()

up = down = left = right = False

#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_UP:
            up = True
        if event.type == KEYDOWN and event.key ==K_w:
            up = True
        if event.type == KEYDOWN and event.key == K_DOWN:
            down = True
        if event.type == KEYDOWN and event.key == K_s:
            down = True
        if event.type == KEYDOWN and event.key == K_LEFT:
            left = True
        if event.type == KEYDOWN and event.key == K_a:
            left = True
        if event.type == KEYDOWN and event.key == K_RIGHT:
            right = True
        if event.type == KEYDOWN and event.key == K_d:
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

    player.update(up, down, left, right)
    collectible.update()
    camera.update()
    pygame.display.flip()
