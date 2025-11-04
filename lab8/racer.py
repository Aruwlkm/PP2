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
coin_img = pygame.transform.scale(coin_img, (35, 35))         # уменьшаем монету
# Начальные позиции игрока
player_x = WIDTH // 2
player_y = HEIGHT - 120

# Начальные позиции врага
baska_x = random.randint(40, WIDTH - 40)
baska_y = 0

# Позиции монеты
coin_x = random.randint(40, WIDTH - 40)
coin_y = -150   # появляется чуть выше экрана

# Счетчик монет
coins_collected = 0

# Шрифт для текста
font = pygame.font.Font(None, 36)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
        player_x += 5

    # Движение врага
    baska_y += 7
    if baska_y > HEIGHT:
        baska_y = 0
        baska_x = random.randint(40, WIDTH - 40)

    # Движение монеты
    coin_y += 5
    # Если монета ушла вниз — появится снова
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(40, WIDTH - 40)

    # Прямоугольники для коллизий
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    baska_rect = pygame.Rect(baska_x, baska_y, baska_img.get_width(), baska_img.get_height())
    coin_rect = pygame.Rect(coin_x, coin_y, coin_img.get_width(), coin_img.get_height())

    # Проверка столкновения с врагом — игра окончена
    if player_rect.colliderect(baska_rect):
        print("Game Over! Coins:", coins_collected)
        pygame.quit()
        sys.exit()

    # Проверка сборa монеты
    if player_rect.colliderect(coin_rect):
        coins_collected += 1
        # Перемещаем монету вверх в новое место
        coin_y = -50
        coin_x = random.randint(40, WIDTH - 40)

    # Очищаем экран
    screen.fill(WHITE)

    # Рисуем объекты
    screen.blit(player_img, (player_x, player_y))
    screen.blit(baska_img, (baska_x, baska_y))
    screen.blit(coin_img, (coin_x, coin_y))

    # Печатаем счетчик монет в верхнем правом углу
    text = font.render("Coins: " + str(coins_collected), True, BLACK)
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))

    pygame.display.update()
    clock.tick(60)