import pygame
import  random

pygame.init()

# color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# game specfic variable
screen_width = 900
screen_height = 600
snake_x = 45
snake_y = 55
snake_size = 10
fps = 60
velocity_x = 0
velocity_y = 0
init_velocity = 5

food_x = random.randint(20, screen_width/2)
food_y = random.randint(20,screen_height/2)
score = 0

## title
pygame.display.set_caption("snake of vikbro")

## GAME SPECIFIC VARIABLE
exit_game = False
game_over = False
gameWindow = pygame.display.set_mode((screen_width, screen_height))

clock  = pygame.time.Clock()

pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])  ### head of snake

#  game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ### we can quit game now  loop come outside
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y =0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x =0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x =  0


    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x -food_x) < 6 and abs(snake_y -food_y)<6:
        score = score + 10
        print("score:",score)
        food_x = random.randint(20, screen_width/2)
        food_y = random.randint(20, screen_height/2)         ## re genrayte food


    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])  ### head of snake
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])  ### foood
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

