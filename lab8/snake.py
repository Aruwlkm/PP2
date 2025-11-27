import pygame
import random
pygame.init()

#размер окна
WIDTH = 600
HEIGHT = 600

#размер клетки (для сетки)
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

#тустер
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# бастапкы параметры змейки
snake =[(10, 10)]          # координаталар (x, y)
dx = 1                     # по x
dy = 0                     # по y

# Начальная еда
def spawn_food():
    # Создаем еду в случайном месте, пока она не попадет на змейку
    while True:
        x = random.randint(0, (WIDTH // CELL) - 1)
        y = random.randint(0, (HEIGHT // CELL) - 1)
        if (x, y) not in snake:
            return (x, y)

food = spawn_food()# тамактын орны

score = 0
level = 1
speed = 5   # бастапкы скорость

font = pygame.font.SysFont(None, 30)

running = True
game_over = False

while running:
    screen.fill(BLACK)

    # Обработчик событий (управление)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Багыттын озгеруы
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != 1:
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN and dy != -1:
                dx = 0
                dy = 1
            elif event.key == pygame.K_LEFT and dx != 1:
                dx = -1
                dy = 0
            elif event.key == pygame.K_RIGHT and dx != -1:
                dx = 1
                dy = 0

    if not game_over:
        # Получаем координаты головы
        head_x, head_y = snake[0]

        #басн козгалтамыз
        head_x += dx
        head_y += dy

        #границадан шыгуды тексеру
        if head_x < 0 or head_x >= WIDTH // CELL or head_y < 0 or head_y >= HEIGHT // CELL:
            game_over = True

        # озимен соктыгысуды тексеру 
        if (head_x, head_y) in snake:
            game_over = True

        # Добавляем голову в начало
        snake.insert(0, (head_x, head_y))

        # Проверяем, съели ли еду
        if (head_x, head_y) == food:
            score += 1

            # Повышение уровня каждые 4 очка
            if score % 4 == 0:
                level += 1
                speed += 2   # жылдамдык арттырамыз

            food = spawn_food()
        else:
            snake.pop()  # убираем хвост, егер тамак жемесе

        # змейка саламыз
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, (x * CELL, y * CELL, CELL, CELL))

        # тамакты саламыз
        fx, fy = food
        pygame.draw.rect(screen, RED, (fx * CELL, fy * CELL, CELL, CELL))

    # денгей мен упайды корсетемиз
    text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    # егер ойын битсе
    if game_over:
        over_text = font.render("GAME OVER (Press Q to Quit)", True, WHITE)
        screen.blit(over_text, (140, 280))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False

    pygame.display.update()
    clock.tick(speed)

pygame.quit()