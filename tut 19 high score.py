import pygame
import random

pygame.init()

# color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# game specfic variable
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

## title
pygame.display.set_caption("snake of vikbro")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)  ### for score on display


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])  ### head of snake

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


#  game loop
def gameloop():
    ##GAME SPECIFIC VARIABLE
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snake_length = 1
    with open("highscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 3
    snake_size = 20
    fps = 60

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("game over !prees enter to continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  ### we can quit game now  loop come outside
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()



        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  ### we can quit game now  loop come outside
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)  ## re genrayte food
                snake_length += 5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("SCORE:" + str(score )+ "  HISCORE:"+ str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])  ### head of snake

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snake_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])  ### foood
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()