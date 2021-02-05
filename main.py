# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
        
    def update(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y=-1
        if keys[pygame.K_DOWN]:
            self.rect.y=+1
        if keys[pygame.K_RIGHT]:
            self.rect.x=+1
        if keys[pygame.K_LEFT]:
            self.rect.x=-1

        

    


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
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


    
    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    # Обновление
    all_sprites.update()
    pygame.display.update()

pygame.quit()