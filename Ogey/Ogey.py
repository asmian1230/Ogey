import pygame
import random
import pygame.mixer

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (128,128,128)
PINK = (255,0,255)
TEAL = (0,255,255)
 

class Background(pygame.sprite.Sprite):
    world_shift = 0
    level_limt= -1000
    def __init__ (self,all_sprites_list):
        self.world_shift = 0
        self.level_limit= -1000
        self.all_sprites_list = all_sprites_list
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Level2.png')
        self.rect =self.image.get_rect()
        self.rect.left,self.rect.top = [0,0]
    def draw(self,screen):
        screen.blit(Background.image,Background.rect)
        self.all_sprites_list.draw(screen)
    def shift_world(self,shift_x):
        self.world_shift += shift_x
        if self.world_shift>self.level_limit:
            for sprite in self.all_sprites_list:
                sprite.rect.x += shift_x
            Background.rect.x += shift_x
        
        
class Object(pygame.sprite.Sprite):

    def __init__(self, image_name, x,y):

        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

 
 
class Player(pygame.sprite.Sprite):

     
    def __init__(self,screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Ogey.png')
        self.rect = self.image.get_rect()
        self.rect.x=10
        self.rect.y=50
        self.vely=0
        self.jump = 1
 
    def update(self,object_list,ogey):
        if self.rect.y <150:
            if self.vely < 148:
                if self.vely<2:
                    self.vely+=1
                else:
                    self.vely=1
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.x > 3:
                self.rect.x -= 3
                if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.x+=3
        if keys[pygame.K_RIGHT]:
            if self.rect.x <776:
                if self.rect.x >388:
                    Background.shift_world(-3)
                self.rect.x+=3
                if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.x -=3
                    if self.rect.x >388:
                        Background.shift_world(3)
                    
        if keys[pygame.K_UP]:
            if self.rect.y > 6:
                if self.jump>0:
                    self.vely-=7
                    self.jump-=1
        if keys[pygame.K_DOWN]:
                self.vely+=1
        if self.rect.y <149:
            self.rect.y+=self.vely
        if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.y-=self.vely
                    self.vely=0
                    if self.jump <2 :
                        self.jump+=1

 
 

pygame.init()
pygame.mixer.init()
 

screen_width = 800
screen_height = 179
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill([255,255,255])

platform1 = Object('Platform.png',300,100)
platform2 = Object('Platform.png',0,100)
screen.blit(platform1.image,platform1.rect)
screen.blit(platform2.image,platform2.rect)
all_sprites_list = pygame.sprite.Group()
 

Object_list = pygame.sprite.Group()
Object_list.add(platform1)
Object_list.add(platform2)
all_sprites_list.add(platform1)
all_sprites_list.add(platform2)





player1 = Player(screen)

all_sprites_list.add(player1)

Background = Background(all_sprites_list)
Background.draw(screen)

done = False
clock = pygame.time.Clock()

player1.rect.y = 60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
    all_sprites_list.update(Object_list,player1)
 

    screen.fill([255,255,255])
    screen.blit(Background.image,Background.rect)
    screen.blit(platform1.image,platform1.rect)
    screen.blit(platform2.image,platform2.rect)
    all_sprites_list.draw(screen)



    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()

