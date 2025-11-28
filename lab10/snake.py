import pygame
from random import randrange
import psycopg2
pygame.init()

#Настройка базы
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_NAME = "snake_db"
DB_PORT = 5433

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)
cur = conn.cursor()

#Проверка пользователя
username = input("Enter your username: ")
cur.execute("SELECT id FROM users WHERE username=%s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]   #бурын тиркелген
    cur.execute("SELECT score, level FROM user_score WHERE user_id=%s", (user_id,))  # Онын сонгы score и level жазбаларын аламыз
    progress = cur.fetchone()
    if progress:
        score, level = progress
        print(f"Welcome back {username}! Score: {score}, Level: {level}")
    else:
        score, level = 0, 1
        print(f"Welcome back {username}! No saved progress yet.")
else:
    # Егер жана колданушы болса — users кестесине косу
    cur.execute("INSERT INTO users(username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    score, level = 0, 1
    conn.commit()
    print(f"New user created: {username}")

# Функция сохранения прогресса
def save_progress(score, level):      # user_score кестесине жазамыз
    cur.execute("""
        INSERT INTO user_score(user_id, score, level)  
        VALUES (%s, %s, %s)
        ON CONFLICT (user_id) DO UPDATE
        SET score = EXCLUDED.score,
            level = EXCLUDED.level
    """, (user_id, score, level))
    conn.commit()     # Егер user_id бурын бар болса UPDATE, болмаса INSERT
    print("Progress saved!")

# Настройка игры
SIZE = 25  
RES=800
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE) # координатты клетка бойыынша туралайды
# Тамактын (кызыл=1, сары=2, күлгин=3)
FOOD_VALUES = [1, 2, 3]
food_value = 1
food_timer = 0
food_max_time = 120
food = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

dirs = {"UP": True, "LEFT": True, "DOWN": True, "RIGHT": True}

length = 1
snake = [(x, y)]
dx, dy = 1, 0       #бастапкы багыт

fps = 15

screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold=True)
font_end = pygame.font.SysFont("Arial", 66, bold=True)
font_level = pygame.font.SysFont("Arial", 26, bold=True)

#Функция появления еды
def spawn_food():
    global food, food_value, food_timer
    food = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    food_value = FOOD_VALUES[randrange(0, len(FOOD_VALUES))]
    food_timer = 0

#Основной цикл
running = True
paused = False

while running:
    screen.fill(pygame.Color("black"))

    #змейка саламыз
    [pygame.draw.rect(screen, pygame.Color("green"), (i, j, SIZE - 2, SIZE - 2)) for i, j in snake]

    #тамак
    food_color = "red" if food_value == 1 else "yellow" if food_value == 2 else "purple"
    pygame.draw.rect(screen, pygame.Color(food_color), (*food, SIZE, SIZE))

    # упай и уровень
    render_score = font_score.render(f"SCORE: {score}", 1, pygame.Color("orange"))
    render_level = font_level.render(f"LEVEL: {level}", 1, pygame.Color("orange"))
    screen.blit(render_score, (5, 5))    # render_score,score деген жазуды суретке айналдырады
    screen.blit(render_level, (5, 30))

    # Движение змейки
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Таймер тамактын
    food_timer += 1
    if food_timer > food_max_time:
        spawn_food()

    # Поедание еды
    if snake[-1] == food:
        length += 1
        score += food_value
        spawn_food()
        if score % 4 == 0: #ар 4 упай сайын  денгей оседи
            level += 1
            fps += 0.5

    # Столкновение
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        save_progress(score, level)
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    conn.close()
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    # Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress(score, level)
            conn.close()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dirs["UP"]:
                dx, dy = 0, -1
                dirs = {"UP": True, "LEFT": True, "DOWN": False, "RIGHT": True}
            if event.key == pygame.K_DOWN and dirs["DOWN"]:
                dx, dy = 0, 1
                dirs = {"UP": False, "LEFT": True, "DOWN": True, "RIGHT": True}
            if event.key == pygame.K_LEFT and dirs["LEFT"]:
                dx, dy = -1, 0
                dirs = {"UP": True, "LEFT": True, "DOWN": True, "RIGHT": False}
            if event.key == pygame.K_RIGHT and dirs["RIGHT"]:
                dx, dy = 1, 0
                dirs = {"UP": True, "LEFT": False, "DOWN": True, "RIGHT": True}
            if event.key == pygame.K_p:  # пауза + сохранение
                paused = not paused
                if paused:
                    save_progress(score, level)
                    print("Game paused!")