import pygame
from datetime import datetime
pygame.display.set_caption("Aruzhan's Mickey game")
pygame.init()
screen = pygame.display.set_mode((1400, 1050))

bg_image = pygame.image.load('./lab7/micky.jpg')
sec_img = pygame.image.load('./lab7/sec.jpg')
min_img = pygame.image.load('./lab7/min.jpg')

x,y=700,525
process = True
while process :
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
    current_time = datetime.now()
    min = current_time.minute
    sec = current_time.second

    angle_sec = -(sec * 6)
    sec_in_img = pygame.transform.rotate(sec_img, angle_sec)
    screen.blit(sec_in_img, (x-sec_in_img.get_width()//2, y-sec_in_img.get_height()//2))

    angle_min=-(min*6+sec*0.1)
    rt_min=pygame.transform.rotate(min_img,angle_min)
    screen.blit(rt_min,(x-rt_min.get_width()//2,y-rt_min.get_height()//2))


    
    font = pygame.font.SysFont('Arial', 36)
    time_text = font.render(current_time.strftime("%H:%M:%S"), True, (255, 0, 0))
    screen.blit(time_text, (50, 50))
    

    pygame.display.flip()
pygame.quit()