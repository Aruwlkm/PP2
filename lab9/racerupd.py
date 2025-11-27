import pygame
import random
import sys
pygame.init()

# Размер окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

#тустер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загружаем картинки
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (50, 100))   # уменьшаем машину игрока
baska_img = pygame.image.load("baska.png")
baska_img = pygame.transform.scale(baska_img, (50, 100))     # уменьшаем машину врага

coin_img = pygame.image.load("coin.png") 

# Начальные позиции игрока
player_x = WIDTH // 2
player_y = HEIGHT - 120 # ойыншынын машинасы томенги жакта туру ушн

# Начальные позиции врага
baska_x = random.randint(40, WIDTH - 40)
baska_y = 0

base_baska_speed = 7 #скорость озгертуге болады
baska_speed = base_baska_speed

# Позиции монеты
coin_x = random.randint(40, WIDTH - 40)
coin_y = -150   # появляется чуть выше экрана

coin_turler=[
    {"name":"small","value": 1,"size":28},
    {"name":"medium","value": 3,"size":40},
    {"name":"big","value": 5, "size": 54}
]

def spawn_coin():
    ctype=random.choice(coin_turler)
    cx=random.randint(40,WIDTH-40)
    cy=-random.randint(50,200)
    return{"x":cx, "y":cy,"type":ctype}
coin=spawn_coin()

# Счетчик монет
coins_collected = 0
# настройки увеличения скорости врага
speed_increase_threshold = 1  # каждые N очков — увеличивать скорость врага
next_speed_threshold = speed_increase_threshold  # следующий порог для увеличения скорости
speed_increment = 1  # на сколько увеличивается скорость врага при достижении порога


# Шрифт для текста
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width(): #ойыншынын экран шегинен шыкпауын кадагалайд
        player_x += 5

    # Движение врага
    baska_y += baska_speed
    if baska_y > HEIGHT: #егер ол экраннан тусип кетсе
        baska_y = -random.randint(50,150)
        baska_x = random.randint(40, WIDTH - 40)# жана позицияда пайда болады

    # Движение монеты
    coin_y += 5
    # Если монета ушла вниз — появится снова
    if coin_y > HEIGHT:
        coin_y = -50  #ол жогарыдан кайтадан пайда болады
        coin_x = random.randint(40, WIDTH - 40)
    coin_fall_speed=4+(2-coin["type"]["value"]/3)

    # чтобы скорость была адекватной, ограничим:
    if coin_fall_speed < 2:
        coin_fall_speed = 2
    if coin_fall_speed > 7:
        coin_fall_speed = 7

    coin["y"] += coin_fall_speed
    # Если монета ушла вниз — появится снова новой рандомной позиции и типа
    if coin["y"] > HEIGHT:
        coin = spawn_coin()

    # Прямоугольники для коллизий
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    baska_rect = pygame.Rect(baska_x, baska_y, baska_img.get_width(), baska_img.get_height())

    current_coin_img = pygame.transform.scale(coin_img, (coin["type"]["size"], coin["type"]["size"]))
    coin_rect = pygame.Rect(coin["x"], coin["y"], current_coin_img.get_width(), current_coin_img.get_height())


    # Проверка столкновения с врагом — игра окончена
    if player_rect.colliderect(baska_rect):
        print("Game Over! Coins:", coins_collected)
        pygame.quit()
        sys.exit()

    # Проверка сборa монеты
    if player_rect.colliderect(coin_rect):
        collected_value = coin["type"]["value"]
        coins_collected += collected_value
        # После сборa — создаём новую монету (рандомный тип/позиция)
        coin = spawn_coin()

         #Проверяем нужно ли увеличить скорость врага (когда суммарные очки превышают порог)
        if coins_collected >= next_speed_threshold:
            baska_speed += speed_increment
            next_speed_threshold += speed_increase_threshold
            # Можно вывести отладочный текст в консоль
            print(f"Speed increased! New baska_speed = {baska_speed}. Next threshold = {next_speed_threshold}")


    # Очищаем экран
    screen.fill(WHITE)

    # Рисуем объекты
    screen.blit(player_img, (player_x, player_y))
    screen.blit(baska_img, (baska_x, baska_y))

    screen.blit(current_coin_img, (coin["x"], coin["y"]))
    # Отображаем значение монеты чуть выше неё
    val_text = small_font.render(str(coin["type"]["value"]), True, BLACK)
    screen.blit(val_text, (coin["x"] + current_coin_img.get_width() // 2 - val_text.get_width() // 2,coin["y"] - 18))

    # Печатаем счетчик монет в верхнем правом углу
    text = font.render("Coins: " + str(coins_collected), True, BLACK)
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))
    
     # (Опционально) показываем текущую скорость врага для отладки/информации
    speed_text = small_font.render(f"Enemy speed: {baska_speed}", True, BLACK)
    screen.blit(speed_text, (10, 10))

    pygame.display.update()
    clock.tick(60)