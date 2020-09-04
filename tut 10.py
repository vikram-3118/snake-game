import pygame

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
fps = 30

## title
pygame.display.set_caption("snake of vikbro")

## GAME SPECIFIC VARIABLE
exit_game = False
game_over = False
gameWindow = pygame.display.set_mode((screen_width, screen_height))

clock  = pygame.time.Clock()


#  game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ### we can quit game now  loop come outside
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 20


    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])  ### head of snake
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

