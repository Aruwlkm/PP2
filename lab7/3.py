import pygame
import sys
 
FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Доппа бірдеңе")
r = 25
x = WIN_WIDTH//2
y = WIN_HEIGHT // 2
 
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    speed=20
    if keys[pygame.K_RIGHT]:
        x +=speed
    if keys[pygame.K_LEFT]:
        x -=speed
    if keys[pygame.K_UP]:
        y -=speed
    if keys[pygame.K_DOWN]:
        y +=speed
 
    # фон
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), r)# круг саламыз
    pygame.display.update()
    clock.tick(FPS)
