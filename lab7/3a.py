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
    if keys[pygame.K_RIGHT] and x+ speed+r<=WIN_WIDTH:
        x +=speed
    if keys[pygame.K_LEFT] and x-speed-r>=0:
        x -=speed
    if keys[pygame.K_UP] and y-speed-r>=0:
        y -=speed
    if keys[pygame.K_DOWN]and y+speed+r<=WIN_HEIGHT:
        y +=speed
 
    # фон
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), r)# круг саламыз
    pygame.display.update()
    clock.tick(FPS)


current_time=datetime.now()
min=current_time.minute
sec=current_time.second
angle_sec=-(sec*6)
sec_in_img=pygame.transform.rotate(sec_img,angle_sec)
screen.blit(sec_in_img,(x-sec_in_img.get_width()//2,y-sec_in_img.get_height()//2))
