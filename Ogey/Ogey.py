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
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('L1-BG.png')
        self.rect =self.image.get_rect()
        self.rect.left,self.rect.top = [0,0]

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
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x > 3:
                self.rect.x -= 3
                if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.x+=3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x <1847:
                self.rect.x += 3
                if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.x -=3
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

music = 'ogey.mid'
pygame.mixer.music.load(music)


screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
Background = Background()
screen.fill([255,255,255])
screen.blit(Background.image,Background.rect)
platform1 = Object('Platform.png',300,150)
platform2 = Object('Platform.png',0,150)
platform3 = Object('Platform.png', 400, 100)
flower1 = Object('flower.png', 200, 75)
trampoline1 = Object('trampoline.png', 140, 190)
heart1 = Object('heart.png', 50, 400)
screen.blit(platform1.image,platform1.rect)
screen.blit(platform2.image,platform2.rect)
screen.blit(platform3.image,platform3.rect)
all_sprites_list = pygame.sprite.Group()


Object_list = pygame.sprite.Group()
Object_list.add(platform1)
Object_list.add(platform2)
Object_list.add(flower1)
Object_list.add(trampoline1)
Object_list.add(heart1)
all_sprites_list.add(platform1)
all_sprites_list.add(platform2)
all_sprites_list.add(flower1)
all_sprites_list.add(trampoline1)
all_sprites_list.add(heart1)




player1 = Player(screen)

all_sprites_list.add(player1)



done = False
clock = pygame.time.Clock()

player1.rect.y = 60
while not done:
    pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
    all_sprites_list.update(Object_list,player1)


screen.fill([255,255,255])
    screen.blit(Background.image,Background.rect)
    screen.blit(platform1.image,platform1.rect)
    screen.blit(platform2.image,platform2.rect)
    screen.blit(platform3.image,platform3.rect)
    all_sprites_list.draw(screen)
    
    
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

