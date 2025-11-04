import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

#тустер
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)

# бастапкы параметры
current_color = BLACK
tool = "brush"   # brush, eraser, rect, circle
brush_size = 5

running = True
drawing = False
start_pos = None  # тиктортбурш и круг ушн

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Начали рисовать мышью
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Отпустили кнопку мыши
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # тиктортбурыш саламыз
            if tool == "rect":
                x1, y1 = start_pos
                x2, y2 = end_pos
                width = x2 - x1
                height = y2 - y1
                pygame.draw.rect(screen, current_color, (x1, y1, width, height), 2)

            # круг саламыз
            if tool == "circle":
                x1, y1 = start_pos
                x2, y2 = end_pos
                radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 2)
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)

        # Выбор инструментов и цвета клавишами
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_e:
                tool = "eraser"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"

            if event.key == pygame.K_1:
                current_color = RED
            if event.key == pygame.K_2:
                current_color = GREEN
            if event.key == pygame.K_3:
                current_color = BLUE

            if event.key == pygame.K_SPACE:
                screen.fill(WHITE)

    # Рисование кистью или ластиком во время движения мыши
    if drawing and tool == "brush":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, current_color, pos, brush_size)

    if drawing and tool == "eraser":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, pos, brush_size)
    pygame.display.update()
pygame.quit()