import pygame
pygame.init()


#CREATING WINDOW
gameWindow = pygame.display.set_mode((1200 , 500))
pygame.display.set_caption("my first game")


## GAME SPECIFIC VARIABLE
exit_game = False
game_over = False


## creating game loop

while not exit_game:            ### it stop the window
    for event in pygame.event.get():     ### it write all touch on mouse and keyword
        print(event)          ### print every event touch

pygame.quit()
quit()

