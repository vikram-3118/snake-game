import pygame
pygame.init()


#CREATING WINDOW
gameWindow = pygame.display.set_mode((1200 , 500))
pygame.display.set_caption("my first game")


## GAME SPECIFIC VARIABLE
exit_game = False
game_over = False


## creating game loop

while not exit_game:             ### it stop the window
    for event in pygame.event.get():     ### it write all touch on mouse and keyword
        print(event)

        if event.type==pygame.QUIT:         ### we can quit game now  loop come outside
            exit_game=True

        if event.type == pygame.KEYDOWN:           ## is any key prace
            if event.key== pygame.K_RIGHT:           ## which key prece
                print("you have presed right arrow key")     ## if above key prace then write

pygame.quit()
quit()