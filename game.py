# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 1080
HEIGHT = 720
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#class gmap:
    #def __init__(self):
        #for x in range(0,5):
        #    for y in range(0,6):
                #if map [x][y]:
               #==1:
               #tile=Tile(x,y)
                all_sprites.add(tile)
       #   self.images=
         # self.rect=self.image.get_rect()
         # self.rect.center=(WIDTH/2,HEIGHT/2)
         # images.appened(sprites)
Class Tile:
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect.center = (x / 2, y / 2)
        self.images=[]

    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/kratos.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
i,x,y = 0,0,0
wall,char ="$","웃"   
xchar,ychar = 8,4
xborder, yborder = 16,8
while True:
    render(xchar,ychar)
        
    d = move()
    wb = wallbang(xborder,yborder,xchar+ d[0],ychar + d[1])
    if wb == True:
        xchar = xchar+d[0]
        ychar = ychar+d[1]  
    print(d)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновлениее
    all_sprites.update()
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
