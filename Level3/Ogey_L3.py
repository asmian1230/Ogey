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
    def __init__ (self,all_sprites_list):
        self.world_shift = 0
        self.level_limit= -2400
        self.all_sprites_list = all_sprites_list
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('L3_Background.png')
        self.rect =self.image.get_rect()
        self.rect.left,self.rect.top = [0,0]
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        self.all_sprites_list.draw(screen)
    def shift_world(self,shift_x):
        self.world_shift += shift_x
        if self.world_shift>self.level_limit:
            for sprite in self.all_sprites_list:
                sprite.rect.x += shift_x
            self.rect.x += shift_x
            if self.rect.x > 800:
                for sprite in self.all_sprites_list:
                    sprite.rect.x -= shift_x
                self.rect.x -= shift_x
        
        
class Object(pygame.sprite.Sprite):

    def __init__(self, image_name, x,y):

        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x
        self.rect.y
        
    def update(self,Object_list):
        self.rect.x += 1
 
 
class Player(pygame.sprite.Sprite):

     
    def __init__(self,screen):
        self.screen = screen
        self.parachute = False
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Ogey.png')
        self.rect = self.image.get_rect()
        self.rect.x=10
        self.rect.y=170
        self.vely=0
        self.jump = 1
    def spike(self,Spike_list):
        self.rect.y+=5
        if pygame.sprite.spritecollideany(self,Spike_list):
            self.rect.y-=5
            return True
        self.rect.y-=5
        
    def update(self,object_list,ogey,background):
        boolean = False
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.x >=5:
                self.rect.x -= 5
                if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.x+=5
        if keys[pygame.K_RIGHT]:
                if self.rect.x <776:
                    self.rect.x+=5
                if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.x -=5
        if keys[pygame.K_UP]:
            if self.rect.y > 6:
                    self.rect.y -= 9
        if keys[pygame.K_DOWN]:
                self.rect.y+=9
        
        if self.rect.y <170:
            if self.rect.y >1:
                self.rect.y+=self.vely
            else :
                self.rect.y+=1
        else :
            background.shift_world(-self.vely)
            if self.rect.y<370:
                self.rect.y+=self.vely
        if pygame.sprite.spritecollideany(ogey,object_list)!=None:
                    self.rect.y-=self.vely
                    background.shift_world(self.vely)
                    if self.jump <2 :
                        if self.vely>0:
                            self.jump+=1
                    self.vely=0


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Boss.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 200
        self.up = 1
    def update(self,Object_list):
        if self.rect.y <= 0:
            self.up = 0
        if self.rect.y >= 300:
            self.up = 1
        if self.up == 1:
            self.rect.y -=3
        else:
            self.rect.y +=3
        if pygame.sprite.spritecollideany(self,Object_list):
            self.up = self.up *-1

        

pygame.init()
pygame.mixer.init()
 
gameover= False
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill([255,255,255])
def game():
   


    all_sprites_list = pygame.sprite.Group()
    Object_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()


    

    player1 = Player(screen)
    boss = Boss()
    
    all_sprites_list.add(boss)
    all_sprites_list.add(player1)
    
    background = Background(all_sprites_list)
    background.draw(screen)

    done = False
    clock = pygame.time.Clock()

    all_sprites_list.draw(screen)
        
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
                done = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                bullet = Bullet()
                bullet.rect.x = player1.rect.x
                bullet.rect.y = player1.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                bullet.update(bullet_list)
        
        player1.update(Object_list,player1,background)
        boss.update(Object_list)
        
        screen.fill([255,255,255])
        screen.blit(background.image,background.rect)
        all_sprites_list.draw(screen)
 
        pygame.display.flip()

        clock.tick(60)
if not gameover:
    game()
pygame.quit()
