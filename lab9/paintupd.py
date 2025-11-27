import pygame
import math
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
tool = "brush"   # brush, eraser, rect, circle,square,rtriangle,etriangle,rhombus
brush_size = 5

running = True
drawing = False
start_pos = None  # фигура салуды бастайтын нукте
font = pygame.font.SysFont(None, 18)

def draw_square(surface, color, start, end, width=2):
    x1, y1 = start
    x2, y2 = end
    w = x2 - x1 #ени
    h = y2 - y1 #биыктыгы
    size = min(abs(w), abs(h)) #квадраттын ени мен биыктиги бирдей болу ушин
    rect_x = x1 if w >= 0 else x1 - size # кай багытка салынатынын ескеру
    rect_y = y1 if h >= 0 else y1 - size
    pygame.draw.rect(surface, color, (rect_x, rect_y, size, size), width)

def draw_right_triangle(surface, color, start, end, width=2):
    # Тік бұрышты үшбұрыш: A = start, B = (end.x, start.y), C = end
    x1, y1 = start  #бурыш старт нуктесинде болады
    x2, y2 = end
    p1 = (x1, y1)
    p2 = (x2, y1)
    p3 = (x2, y2)
    pygame.draw.polygon(surface, color, [p1, p2, p3], width)

def draw_equilateral(surface, color, start, end, width=2):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    base_len = math.hypot(dx, dy) # негиз узындыгы
    if base_len == 0:
        return
    height = (3**0.5) / 2 * base_len #биыктиги
    nx = -dy / base_len #перпендикуляр вектор
    ny = dx / base_len
    mx = (x1 + x2) / 2 #негиздин ортасы
    my = (y1 + y2) / 2
    apex = (mx + nx * height, my + ny * height) # ушинши тобе
    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), apex], width)

def draw_rhombus(surface, color, start, end, width=2):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) / 2 # ортасы
    cy = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    diag_len = math.hypot(dx, dy)
    if diag_len == 0:
        return
    # Перпендикуляр багыт
    px = -dy / diag_len
    py = dx / diag_len
    half_dx = dx / 2 # Жарты диагональдар
    half_dy = dy / 2
    half_px = px * (diag_len / 2)
    half_py = py * (diag_len / 2)
    v1 = (cx - half_dx, cy - half_dy)
    v2 = (cx + half_px, cy + half_py)
    v3 = (cx + half_dx, cy + half_dy)
    v4 = (cx - half_px, cy - half_py)
    pygame.draw.polygon(surface, color, [v1, v2, v3, v4], width)

def draw_help(): #умытып калса
    lines = [
        "B - brush, E - eraser, R - rect, S - square",
        "T - right triangle, Y - equilateral triangle, H - rhombus, C - circle",
        "1/2/3 - RED/GREEN/BLUE, SPACE - clear"
    ]
    help_width = 760
    help_height = 70
    help_x = 20
    help_y = 5
    pygame.draw.rect(screen, (230, 230, 230), (help_x, help_y, help_width, help_height),border_radius=8)# фонды салу
    pygame.draw.rect(screen, (80, 80, 80), (help_x, help_y, help_width, help_height),2,border_radius=8) # рамка салу
    y_offset=help_y +10
    for line in lines:
        text_surface=font.render(line,True,(40,40,40))
        screen.blit(text_surface,(help_x +10,y_offset))
        y_offset += 22
 # негизги цикл
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
            elif tool == "circle":
                x1, y1 = start_pos
                x2, y2 = end_pos
                radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 2)
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)

            elif tool == "square":
                draw_square(screen, current_color, start_pos, end_pos, width=2)

            elif tool == "rtriangle":
                draw_right_triangle(screen, current_color, start_pos, end_pos, width=2)

            elif tool == "etriangle":
                draw_equilateral(screen, current_color, start_pos, end_pos, width=2)

            elif tool == "rhombus":
                draw_rhombus(screen, current_color, start_pos, end_pos, width=2)


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
            if event.key == pygame.K_s:
                tool = "square"
            if event.key == pygame.K_t:
                tool = "rtriangle"
            if event.key == pygame.K_y:
                tool = "etriangle"
            if event.key == pygame.K_h:
                tool = "rhombus"

            if event.key == pygame.K_1:
                current_color = RED
            if event.key == pygame.K_2:
                current_color = GREEN
            if event.key == pygame.K_3:
                current_color = BLUE

            if event.key == pygame.K_SPACE:   # Очистить экран
                screen.fill(WHITE)

    # Рисование кистью или ластиком во время движения мыши
    if drawing and tool == "brush":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, current_color, pos, brush_size)

    if drawing and tool == "eraser":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, pos, brush_size)
    draw_help()
    pygame.display.update()
pygame.quit()