import pygame, random
pygame.init()
#  Экран параметрлері
W, H = 600, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Fruit Catch")
clock = pygame.time.Clock()

#  Бастапқы объектілер
basket_x = 250                 # корзинаның X координатасы
fruit_x = random.randint(0, 580)  # жемістің X позициясы (рандом)
fruit_y = -20                     # жеміс экраннан жоғарыда басталады
fruit_speed = 5                   # жемістің түсу жылдамдығы

score = 0                         # жиналған ұпай
game_over = False                # ойын бітті ме?

font = pygame.font.SysFont(None, 40)  # мәтін шрифті

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:     # терезені жабу
            running = False

        #  Game Over режиміндегі басқару
        if game_over:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
            # ОЙЫНДЫ ҚАЙТА БАСТАУ
                    basket_x = 250
                    fruit_x = random.randint(0, 580)
                    fruit_y = -20
                    score = 0
                    game_over = False

                if e.key == pygame.K_q:
                    running = False   # шығу

    #  НЕГІЗГІ ОЙЫН ЛОГИКАСЫ (game_over == False)
    if not game_over:
        #  Корзинаны басқару
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= 7
        if keys[pygame.K_RIGHT] and basket_x < W - 80:
            basket_x += 7

        #  Жемістің түсуі
        fruit_y += fruit_speed
        #  Егер жеміс жерге тисе → Game Over
        if fruit_y > H:
            game_over = True
        #  Коллизияны тексеру (ұстау)
        basket_rect = pygame.Rect(basket_x, 550, 80, 20)    # корзина тік төртбұрыш
        fruit_rect = pygame.Rect(fruit_x, fruit_y, 20, 20)  # жемістің тік төртбұрыш

        if basket_rect.colliderect(fruit_rect):
            score += 1          # ұпай қосылады
            fruit_y = -20       # жеміс қайта жоғардан басталады
            fruit_x = random.randint(0, 580)
        #  Экранды салу

        screen.fill((255, 255, 255))

        # корзина
        pygame.draw.rect(screen, (0, 0, 255), (basket_x, 550, 80, 20))

        # жеміс
        pygame.draw.circle(screen, (255, 0, 0), (fruit_x, fruit_y), 10)

        # ұпай
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        screen.blit(score_text, (10, 10))

    #  GAME OVER ЭКРАНЫ
    else:
        screen.fill((0, 0, 0))

        over = font.render("GAME OVER", True, (255, 0, 0))
        scr  = font.render(f"Your Score: {score}", True, (255, 255, 255))
        hint = font.render("Press R to Restart | Q to Quit", True, (255, 255, 255))

        # мәтінді экран ортасына шығару
        screen.blit(over, (W//2 - over.get_width()//2, 220))
        screen.blit(scr, (W//2 - scr.get_width()//2, 280))
        screen.blit(hint, (W//2 - hint.get_width()//2, 340))
    #  Экранды жаңарту
    pygame.display.update()
    clock.tick(60)

pygame.quit()
