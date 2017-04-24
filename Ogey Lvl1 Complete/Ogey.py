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
        self.image = pygame.image.load('Level1.png')
        self.rect =self.image.get_rect()
        self.rect.left,self.rect.top = [0,0]
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        self.all_sprites_list.draw(screen)
    def shift_world(self,shift_y):
        self.world_shift += shift_y
        if self.world_shift>self.level_limit:
            for sprite in self.all_sprites_list:
                sprite.rect.y += shift_y
            self.rect.y += shift_y
            if self.rect.y > 0:
                for sprite in self.all_sprites_list:
                    sprite.rect.y -= shift_y
                self.rect.y -= shift_y
        
        
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
    def upparachute(self):
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load('Parachute-ogey.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self,object_list,ogey,background):
        boolean = False
        if self.rect.y <400:
                if self.vely<2:
                    self.vely+=1
                elif self.parachute==False :
                    self.vely=5
                else:
                    self.vely=1
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
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if self.rect.y > 6:
                    if self.jump>0:
                        self.vely-=9
                        self.jump-=1
        if keys[pygame.K_DOWN]:
                self.vely+=1
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
class Heart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = 152
        self.rect.y = 575
        self.up = 1
    def update(self,Object_list):
        if self.up == 1:
            self.rect.y -=1
        else:
            self.rect.y +=1
        if pygame.sprite.spritecollideany(self,Object_list):
            self.up = self.up *-1

        
class Flower(pygame.sprite.Sprite):
     def __init__(self,image_name,x,y,num):
        self.num = num
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
 
class Parachute(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Parachute.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 1450
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Ogey falls in love.mid")
pygame.mixer.music.play(-1)
 
gameover= False
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill([255,255,255])
def game():
    Platform_list = pygame.sprite.Group()
    Spike_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    Object_list = pygame.sprite.Group()
    Flower_list = pygame.sprite.Group()
    platform1 = Object('Platform.png',625,200)
    platform2 = Object('Platform.png',0,200)
    platform3 = Object('Platform2.png',300,200)
    platform30 = Object('Platform.png',455,210)
    platform4 = Object('Platform3.png',425,105)
    platform5 = Object('Platform2.png',455,105)
    platform6 = Object('Platform2.png',0,400)
    platform7 = Object('Platform2.png',440,400)
    platform8 = Object('Platform2.png',0,600)
    platform9 = Object('Platform.png',625,600)
    platform10 = Object('Platform.png',450,600)
    platform11 = Object('Platform.png',275,600)
    platform12 = Object('Platform.png',0,755)
    platform13 = Object('Platform3.png',350,630)
    platform14 = Object('Platform2.png',255,755)
    platform31 = Object('Platform2.png',155,765)
    platform15 = Object('Platform2.png',555,720)
    platform16 = Object('Platform2.png',660,850)
    platform17 = Object('Platform2.png',430,950)
    platform18 = Object('Platform2.png',660,1050)
    platform19 = Object('Platform2.png',410,1140)
    platform20 = Object('Platform2.png',0,1250)
    platform21 = Object('Platform2.png',125,1270)
    platform22 = Object('Platform2.png',250,1250)
    platform23 = Object('Platform2.png',375,1250)
    platform24 = Object('Platform.png',500,1250)
    platform25 = Object('Platform2.png',675,1250)
    platform26 = Object('Platform.png',100,1400)
    platform27 = Object('Platform3.png',470,1425)
    platform28 = Object('Platform2.png',500,1550)
    platform29 = Object('Platform.png',625,1550)
    platform32 = Object('Platform3.png',350,785)
    platform33 = Object('Platform3.png',350,890)
    platform34 = Object('Platform3.png',0,2675)
    platform35 = Object('Platform2.png',650,2770)
    lily = Object('Lily.png',700,2735)

    spikes1 = Object('Spikes2.png',125,350)
    spikes2 = Object('Spikes2.png',280,350)
    spikes3 = Object('Spikes2.png',367,1172)
    spikes4 = Object('Spikes2.png',500,1172)
    spikes5 = Object('Spikes2.png',655,1172)
    spikes6 = Object('Spikes2.png',0,1650)
    spikes7 = Object('Spikes2.png',300,1650)
    spikes8 = Object('Spikes2.png',455,1650)
    spikes9 = Object('Spikes2.png',610,1650)
    spikes10 = Object('Spikes2.png',0,1850)
    spikes11 = Object('Spikes2.png',165,1850)
    spikes12 = Object('Spikes2.png',465,1850)
    spikes13 = Object('Spikes2.png',620,1850)
    spikes14 = Object('Spikes2.png',155,2150)
    spikes15 = Object('Spikes2.png',310,2150)
    spikes16 = Object('Spikes2.png',465,2150)
    spikes17 = Object('Spikes2.png',620,2150)
    spikes18 = Object('Spikes2.png',0,2500)
    spikes19 = Object('Spikes2.png',155,2500)
    spikes20 = Object('Spikes2.png',310,2500)
    spikes21 = Object('Spikes2.png',645,2500)
    spikes22 = Object('Spikes2.png',100,910)
    spikes23 = Object('Spikes2.png',670,522)

    flower1 = Flower('Flower.png',490,80,1)
    flower2 = Flower('Flower.png',40,575,2)
    flower3 = Flower('Flower.png',595,695,3)


    Platform_list.add(platform1)
    Platform_list.add(platform2)
    Platform_list.add(platform3)
    Platform_list.add(platform4)
    Platform_list.add(platform5)
    Platform_list.add(platform6)
    Platform_list.add(platform7)
    Platform_list.add(platform8)
    Platform_list.add(platform9)
    Platform_list.add(platform10)
    Platform_list.add(platform11)
    Platform_list.add(platform12)
    Platform_list.add(platform13)
    Platform_list.add(platform14)
    Platform_list.add(platform15)
    Platform_list.add(platform16)
    Platform_list.add(platform17)
    Platform_list.add(platform18)
    Platform_list.add(platform19)
    Platform_list.add(platform20)
    Platform_list.add(platform21)
    Platform_list.add(platform22)
    Platform_list.add(platform23)
    Platform_list.add(platform24)
    Platform_list.add(platform25)
    Platform_list.add(platform26)
    Platform_list.add(platform27)
    Platform_list.add(platform28)
    Platform_list.add(platform29)
    Platform_list.add(platform30)
    Platform_list.add(platform31)
    Platform_list.add(platform32)
    Platform_list.add(platform33)
    Platform_list.add(platform34)
    Platform_list.add(platform35)
    Platform_list.add(lily)

    Spike_list.add(spikes1)
    Spike_list.add(spikes2)
    Spike_list.add(spikes3)
    Spike_list.add(spikes4)
    Spike_list.add(spikes5)
    Spike_list.add(spikes6)
    Spike_list.add(spikes7)
    Spike_list.add(spikes8)
    Spike_list.add(spikes9)
    Spike_list.add(spikes10)
    Spike_list.add(spikes11)
    Spike_list.add(spikes12)
    Spike_list.add(spikes13)
    Spike_list.add(spikes14)
    Spike_list.add(spikes15)
    Spike_list.add(spikes16)
    Spike_list.add(spikes17)
    Spike_list.add(spikes18)
    Spike_list.add(spikes19)
    Spike_list.add(spikes20)
    Spike_list.add(spikes21)
    Spike_list.add(spikes22)
    Spike_list.add(spikes23)

    Flower_list.add(flower1)
    Flower_list.add(flower2)
    Flower_list.add(flower3)






    for platform in Platform_list:
        screen.blit(platform.image,platform.rect)
        all_sprites_list.add(platform)
        Object_list.add(platform)
    for spike in Spike_list:
        screen.blit(spike.image,spike.rect)
        all_sprites_list.add(spike)
        Object_list.add(spike)

    for flower in Flower_list:
        screen.blit(flower.image,flower.rect)
        all_sprites_list.add(flower)


    player1 = Player(screen)
    heart = Heart()
    parachute = Parachute()
    all_sprites_list.add(parachute)
    all_sprites_list.add(heart)
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
        player1.update(Object_list,player1,background)
        heart.update(Object_list)
        if pygame.sprite.collide_rect(player1,heart):
            gameover = True
            done = True
            game()
        screen.fill([255,255,255])
        screen.blit(background.image,background.rect)
        all_sprites_list.draw(screen)
        if pygame.sprite.collide_rect(player1,parachute):
            player1.upparachute()
            player1.parachute=True
            all_sprites_list.remove(parachute)
        if player1.spike(Spike_list):
            gameover = True
            done = True
            game()
        for flower in Flower_list:
            if pygame.sprite.collide_rect(player1,flower):
                if flower.num == 1:
                    all_sprites_list.remove(flower1)
                    Flower_list.remove(flower1)
                    all_sprites_list.remove(platform30)
                    Object_list.remove(platform30)
                if flower.num == 2:
                    all_sprites_list.remove(flower2)
                    Flower_list.remove(flower2)
                    all_sprites_list.remove(platform31)
                    Object_list.remove(platform31)
                if flower.num == 3:
                    all_sprites_list.remove(flower3)
                    Flower_list.remove(flower3)
                    all_sprites_list.remove(platform21)
                    Object_list.remove(platform21)
        pygame.display.flip()

        clock.tick(60)
if not gameover:
    game()
pygame.quit()

