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
snake = [(10, 10)]          # координаталар (x, y)
dx = 1                      # по x
dy = 0                      # по y

food_turler = [
    {"value": 1, "color": (180, 0, 0), "size": CELL - 4, "lifetime": 5000},   # 1упай, 7сек
    {"value": 3, "color": (0, 120, 0), "size": CELL - 2, "lifetime": 7000},   # 3 упай, 9сек
    {"value": 5, "color": (200, 180, 0), "size": CELL,     "lifetime": 9000},# 5упай, 11сек
]

# Начальная еда
def spawn_food():
    # Создаем еду в случайном месте, пока она не попадет на змейку
    while True:
        x = random.randint(0, (WIDTH // CELL) - 1)
        y = random.randint(0, (HEIGHT // CELL) - 1)
        if (x, y) not in snake:
            food_type = random.choice(food_turler)
            # ВОТ ТУТ ВАЖНО: возвращаем словарь (dict), чтобы потом можно было использовать food["pos"], food["type"], food["spawn_time"]
            return {"pos": (x, y), "type": food_type, "spawn_time": pygame.time.get_ticks()}

# инициализация первой еды (теперь food — dict)
food = spawn_food()  # тамактын орны

score = 0
level = 1
speed = 7   # бастапкы скорость

font = pygame.font.SysFont(None, 30)
small_font = pygame.font.SysFont(None, 20)
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
        if (head_x, head_y) == food["pos"]:
            collected_value = food["type"]["value"]
            score += collected_value

            # Повышение уровня каждые 4 очка
            if score % 4 == 0:
                level += 1
                speed += 2   # жылдамдык арттырамыз

            food = spawn_food()
        else:
            snake.pop()  # убираем хвост, егер тамак жемесе

        #Проверяем таймер жизни текущей еды
        current_time = pygame.time.get_ticks()
        elapsed = current_time - food["spawn_time"]
        # Если еда живёт дольше своей lifetime — исчезает и появляется новая
        if elapsed > food["type"]["lifetime"]:
            food = spawn_food()

        # змейка саламыз
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, (x * CELL, y * CELL, CELL, CELL))

        # тамакты саламыз
        fx, fy = food["pos"]
        ftype = food["type"]
        fsize = ftype["size"]
        # Рисуем квадрат еды, центрируем внутри клетки
        offset = (CELL - fsize) // 2
        pygame.draw.rect(screen, ftype["color"], (fx * CELL + offset, fy * CELL + offset, fsize, fsize))
        
        # Рисуем значение еды (value) внутри/над ней
        val_surf = small_font.render(str(ftype["value"]), True, WHITE)
        # позиция числа — по центру квадрата еды
        text_x = fx * CELL + offset + fsize // 2 - val_surf.get_width() // 2
        text_y = fy * CELL + offset + fsize // 2 - val_surf.get_height() // 2
        screen.blit(val_surf, (text_x, text_y))

        # Рисуем таймер (сколько миллисекунд осталось -> секунды)
        remaining_ms = max(0, ftype["lifetime"] - elapsed)
        remaining_s = remaining_ms // 1000  # в секундах (целые)
        timer_surf = small_font.render(f"{remaining_s}s", True, WHITE)
        # покажем таймер чуть выше еды
        screen.blit(timer_surf, (fx * CELL + CELL//2 - timer_surf.get_width()//2, fy * CELL - 18))

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
