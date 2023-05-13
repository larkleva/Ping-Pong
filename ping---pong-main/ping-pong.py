from pygame import *
import os


window = display.set_mode((500, 500))
display.set_caption('пинг-понг')


dir = os.path.dirname(os.path.realpath(__file__))


game = True
over = False



class GameSprite(sprite.Sprite):
    def __init__(self, image_str, x, y, speed, wh):
        
        self.image = transform.scale(image.load(image_str), wh)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):    window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__(self,image_str, x,y, speed, wh, up, down):
        super().__init__(image_str, x,y, speed, wh)
        self.up = up
        self.down = down
        self.score = 0

    def update(self):
        self.reset()
        
        k = key.get_pressed()
        global over
       
        if k[self.up] and self.rect.y>0 and over!=True:
            self.rect.y-=self.speed
        
        if k[self.down] and self.rect.y<385 and over!=True:
            self.rect.y+=self.speed
        


class Circle(GameSprite):
    def __init__(self,image_str, x,y, speed, wh):
        super().__init__(image_str, x,y, speed, wh)
        self.speed_y = 1
    def update(self):
        if (over==True): return
        self.reset()
        self.rect.x-=self.speed
        self.rect.y-= self.speed_y
        if (sprite.collide_rect(player_1, self) or sprite.collide_rect(player_2, self)):
            self.speed*=-1
        if (self.rect.y<0 or self.rect.y>465):
            self.speed_y*=-1
    
   
    def respawn(self):
        self.rect.x = 250
        self.rect.y = 250
            



clock = time.Clock()
FPS = 60

bakcground = transform.scale(image.load(dir+"/background.png"), (500, 500))
player_1 = Player(dir+"/player.png", 10,210, 5,(32, 120), K_w, K_s)
player_2 = Player(dir+"/player.png", 455,210, 5,(32, 120), K_UP, K_DOWN)
circle = Circle(dir+'/circle.png', 250, 250, 8, (32,32))


font.init()
font1 = font.Font(None, 50)


lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 50)

lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    window.blit(bakcground, (0,0))

    player_1.update()
    player_2.update()
    circle.update()


    if (circle.rect.x<0):
        over = True   
        if (over):
            window.blit(lose1, (125, 250))
        


    if (circle.rect.x>485):
        over = True
        if (over):
            window.blit(lose2, (125, 250))



    clock.tick(FPS)
    display.update()
